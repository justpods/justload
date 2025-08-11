from pathlib import Path

from justload.main import login


def test_login(testpath: Path):
    login()
