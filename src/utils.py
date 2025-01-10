from glob import glob

from instaloader import Instaloader, Post, load_structure_from_file


def offline_posts(l: Instaloader, profile: str):
    return set(
        filter(
            lambda s: isinstance(s, Post),
            (
                load_structure_from_file(l.context, file)
                for file in (
                    glob(f'../data/{profile}/*.json.xz')
                    + glob(f'../data/{profile}/*.json')
                )
            )
        )
    )
