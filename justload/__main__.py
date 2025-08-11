from functools import partial

import click

from .__about__ import __version__
from .providers.youtube import YoutubeLoader

st_bold = partial(click.style, bold=True)
st_bold_red = partial(click.style, bold=True, fg="red")
st_bold_green = partial(click.style, bold=True, fg="green")
echo = click.echo


@click.group()
def cli() -> None:
    """Main Just a Loader CLI."""


@cli.command("version")
def version() -> None:
    echo(__version__)


@cli.command("yt")
@click.argument(
    "url",
)
def youtube(url: str):
    YoutubeLoader(url=url).load(path=".")


if __name__ == "__main__":
    cli()
