
<img src='./thumbnail.png' width='100%'>


## How to install:
- **Dependencies Installation**: To install the necessary dependencies for the script, run the following command:
  ```bash
  pip install -r requirements.txt
  ```
- Run the script locally and input the YouTube video URL to download the video.
- If you want to search youtube video in terminal itself, you can use the [`video_search.py`](https://github.com/apollxo/youtubeVideoDownload/blob/main/video_search.py) script.


## Features:

- **Download Videos**: By providing the YouTube video URL, the software will download both the video and audio streams and merge them into a single file.
  
- **Search YouTube Videos**: With the [`video_search.py`](https://github.com/apollxo/youtubeVideoDownload/blob/main/video_search.py) script, you can search for YouTube videos directly from the terminal. The script will return the URLs of the search results.

- **Simple Dependency**: The software relies on a single Python package for its functionality:
pytube: This package is essential for fetching and downloading YouTube videos. The software specifically uses version 12.1.3 of pytube.

- **User-Friendly Prompts**: The software provides clear prompts to the user for inputting the YouTube video URL or the name of the video they wish to search for.

- **Merging Audio and Video**: After downloading the separate audio and video streams, the software uses ffmpeg to merge them into a single MP4 file.

- **Clean-Up**: Once the video and audio streams are merged, the software automatically deletes the separate downloaded files, leaving only the final merged video.
