import os
from datetime import datetime
from itertools import dropwhile, takewhile

from dotenv import load_dotenv
from instaloader import Instaloader, Profile


load_dotenv()

PROFILE: str = os.getenv("PROFILE_NAME")
L = Instaloader()


def load_profile_sort_by_like():
    profile = Profile.from_username(L.context, PROFILE)
    posts_sorted_by_likes = sorted(
        profile.get_posts(),
        key=lambda p: p.likes + p.comments,
        reverse=True,
    )
    selected_range = posts_sorted_by_likes[0:2]

    for post in selected_range:
        L.download_post(post, target=f"../data/{PROFILE}")


def load_profile_from_period(
    start_date: datetime,
    end_date: datetime,
) -> None:
    """Load profile post with range between start and end datetime objects.

    :param start_date:
    :param end_date:
    """
    profile = Profile.from_username(L.context, PROFILE)
    posts = profile.get_posts()

    for post in takewhile(
        lambda p: p.date > end_date,
        dropwhile(lambda p: p.date > start_date, posts)
    ):
        print(post.date)
        L.download_post(post, target=f"../data/{PROFILE}")


if __name__ == '__main__':
    load_profile_sort_by_like()
    # load_profile_from_period(
    #     start_date=datetime(2025, 12, 1),
    #     end_date=datetime(2025, 12, 2),
    # )
