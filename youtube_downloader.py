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
