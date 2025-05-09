import os
from pathlib import Path
from datetime import datetime
from itertools import dropwhile, takewhile

from dotenv import load_dotenv
from instaloader import Instaloader, Profile


load_dotenv()

PROFILE: str = os.getenv("PROFILE_NAME")


def login() -> Instaloader:
    loader = Instaloader(
        # download_pictures=True,
        # save_metadata=True,
        # compress_json=True,
        quiet=False,
    )
    session_path: Path = Path(f".session")
    session_path.mkdir(exist_ok=True, parents=True)
    session_file: Path = session_path / f"session-{os.getenv('SELF_USER')}"
    if session_file.exists():
        loader.load_session_from_file(os.getenv("SELF_USER"), str(session_file))
    else:
        # loader.interactive_login(username=os.getenv("SELF_USER"))
        loader.login(
            user=os.getenv("SELF_USER"),
            passwd=os.getenv("SELF_PASS"),
        )
        loader.save_session_to_file(session_file)

    print(loader)
    return loader



def load_profile_sort_by_like():
    # loader = login()
    loader = Instaloader()
    profile = Profile.from_username(loader.context, PROFILE)
    posts_sorted_by_likes = sorted(
        profile.get_posts(),
        key=lambda p: p.likes + p.comments,
        reverse=True,
    )
    selected_range = posts_sorted_by_likes[0:2]

    for post in selected_range:
        loader.download_post(post, target=f"./data/{PROFILE}")


def load_profile_from_period(
    start_date: datetime,
    end_date: datetime,
) -> None:
    """Load profile post with range between start and end datetime objects.

    :param start_date: A start datetime
    :param end_date: An end datetime
    """
    loader = login()
    profile = Profile.from_username(loader.context, PROFILE)
    posts = profile.get_posts()

    for post in takewhile(
        lambda p: p.date > end_date,
        dropwhile(lambda p: p.date > start_date, posts)
    ):
        print(post.date)
        loader.download_post(post, target=f"../data/{PROFILE}")


class Instagram:
    """Instagram download wrapper object."""

    def __init__(self, name: str, session_path: Path | None = None) -> None:
        self.name: str = name
        self.loader: Instaloader = self.login(
            session_path or Path("../.session")
        )

    @classmethod
    def login(cls, session_path: Path) -> Instaloader:
        loader = Instaloader(
            download_pictures=True,
            save_metadata=True,
            compress_json=True,
            quiet=False,
        )
        session_path.mkdir(exist_ok=True, parents=True)
        session_file: Path = session_path / f"session-{os.getenv('SELF_USER')}"
        if session_file.exists():
            loader.load_session_from_file(os.getenv("SELF_USER"), str(session_file))
        else:
            # loader.interactive_login(username=os.getenv("SELF_USER"))
            loader.login(
                user=os.getenv("SELF_USER"),
                passwd=os.getenv("SELF_PASS"),
            )
            loader.save_session_to_file(session_file)

        return loader

    def load_top_likes(self, limit: int = 2) -> None:
        profile = Profile.from_username(self.loader.context, self.name)
        posts_sorted_by_likes = sorted(
            profile.get_posts(), key=lambda p: p.likes, reverse=True
        )
        # NOTE: Download from only limit number posts
        selected_range = posts_sorted_by_likes[0:limit]
        for post in selected_range:
            self.loader.download_post(post, target=f"../data/{self.name}")


if __name__ == '__main__':
    # load_profile_sort_by_like()
    # load_profile_from_period(
    #     start_date=datetime(2025, 12, 1),
    #     end_date=datetime(2025, 12, 2),
    # )
    # login()
    load_profile_sort_by_like()
