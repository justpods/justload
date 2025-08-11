import yt_dlp

def download_4k_video_yt_dlp(url, save_path='.'):
    ydl_opts: dict[str, str] = {
        # 'format': 'bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/best[ext=mp4]',
        'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        'outtmpl': f'{save_path}/%(title)s-%(id)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")


class YtDlpLoader:
    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=qtLEETBxznU"
    download_4k_video_yt_dlp(video_url)