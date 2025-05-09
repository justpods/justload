import os

from src.main import Instagram, load_profile_sort_by_like


def test_func_load_profile_sort_by_like():
    load_profile_sort_by_like()


def test_load_top_likes():
    inst = Instagram(name=os.getenv("PROFILE_NAME"))
    inst.load_top_likes(limit=1)
