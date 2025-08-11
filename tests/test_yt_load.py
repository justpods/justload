from pathlib import Path

from pytube import YouTube


def download_4k_video(url, save_path='.'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res="2160p", file_extension='mp4').first()
        if stream:
            print(f"Downloading: {yt.title}")
            stream.download(output_path=save_path)
            print("Download complete!")
        else:
            print("4K stream not available for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_tubfix_highest(url, save_path="."):
    """

    ffmpeg -i videoplayback.mp4 -i videoplayback.m4a -c:v copy -c:a copy output.mp4
    ffmpeg -i 250804.mp4 -i 250804.m4a -c:v copy -c:a copy output.mp4
    """
    from pytubefix import YouTube, Stream
    from pytubefix.cli import on_progress

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    # for l in yt.streams.filter(only_audio=True):
    ys_video_highest: Stream = yt.streams.get_highest_resolution(progressive=False)
    print(ys_video_highest)
    ys_audio_highest: Stream = max(yt.streams.filter(type="audio"), key=lambda x: x.filesize)
    print(ys_audio_highest)
    # print("---")
    # for l in yt.streams.filter(file_extension='mp4'):
    #     print(l)

    # ys = yt.streams.get_by_itag(401)
    # ys.download(output_path=save_path)
    ys_audio_highest.download(output_path=save_path, filename="test")



def test_youtube_load():
    download_4k_video("https://www.youtube.com/watch?v=qtLEETBxznU")


def test_youtube_load_highest(test_path: Path):
    download_tubfix_highest(
        "https://www.youtube.com/watch?v=qtLEETBxznU",
        save_path=str((test_path.parent / "data/youtube").absolute())
    )
