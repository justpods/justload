from instaloader import Instaloader

from justload.utils import offline_posts


def test_offline_posts(installer: Instaloader, profile: str):
    rs = offline_posts(l=installer, profile=profile)
    print(rs)
