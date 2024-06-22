### YouTube Video Downloader

This script allows you to download videos from YouTube or YouTube Shorts using `yt_dlp`.

#### Features
- Download video or audio only
- Specify download format
- Set quality limit
- Custom directory for saving downloads

### Prerequisites

- Python 3.x
- `yt_dlp` library
- `FFmpeg` (required for audio extraction)

### Installation

1. Install `yt_dlp`:
    ```sh
    pip install yt-dlp
    ```

2. Install `FFmpeg`:
    - On Windows, download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.
    - On macOS, install using Homebrew:
      ```sh
      brew install ffmpeg
      ```
    - On Linux, install using your package manager, e.g.:
      ```sh
      sudo apt-get install ffmpeg
      ```

### Usage

Save the script below to a file, e.g., `download_video.py`.

```python
import yt_dlp
import os

def download_video(url, format='best', directory='downloads', audio_only=False, quality_limit=None):
    """
    Downloads a video from YouTube or YouTube Shorts.
    
    :param url: URL of the video
    :param format: Download format ('best', 'worst', or a specific format)
    :param directory: Directory where the video will be saved
    :param audio_only: If True, downloads only the audio
    :param quality_limit: Quality limit (e.g. '720p')
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else format,
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'progress_hooks': [show_progress],
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    if quality_limit:
        ydl_opts['format'] += f'[height<={quality_limit[:-1]}]'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nDownload completed. File saved in {directory}")
    except Exception as e:
        print(f"Error downloading the video: {str(e)}")

def show_progress(d):
    if d['status'] == 'finished':
        print('\nDownload completed. Processing...')
    elif d['status'] == 'downloading':
        p = d['_percent_str']
        print(f'\rDownloading: {p}', end='')

# Usage example
video_url = "https://www.youtube.com/shorts/AQQV3K-BvLg"
download_video(video_url, format='best', directory='my_videos', audio_only=False, quality_limit='720p')
```

### Running the Script

1. Save the script to a file, e.g., `download_video.py`.
2. Run the script:
    ```sh
    python download_video.py
    ```
3. The script will download the specified video and save it in the specified directory.

### Parameters

- `url`: URL of the YouTube video or YouTube Short.
- `format`: Download format (default: `'best'`).
- `directory`: Directory where the video will be saved (default: `'downloads'`).
- `audio_only`: If `True`, downloads only the audio (default: `False`).
- `quality_limit`: Quality limit, e.g., `'720p'` (default: `None`).

### Example

```python
video_url = "https://www.youtube.com/shorts/AQQV3K-BvLg"
download_video(video_url, format='best', directory='my_videos', audio_only=False, quality_limit='720p')
```

This example downloads the video in the best available format, saves it in the `my_videos` directory, and limits the quality to 720p.
