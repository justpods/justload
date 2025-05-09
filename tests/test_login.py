from pathlib import Path

from src.main import login


def test_login(testpath: Path):
    login()
