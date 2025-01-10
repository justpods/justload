import os

import pytest
from dotenv import load_dotenv
from instaloader import Instaloader


load_dotenv()


@pytest.fixture(scope='session')
def installer():
    L = Instaloader()
    return L


@pytest.fixture(scope='session')
def profile() -> str:
    return os.getenv("PROFILE_NAME")
