# Created by SezerBozkir <admin@sezerbozkir.com> at 10/31/2019


import sys
import os
from utils import download_from_link


if __name__ == '__main__':
    if os.name == "nt":
        saving_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        saving_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
    # download_from_link(link)
    if len(sys.argv) != 3:
        print(
            "Using: python youtubex.py <youtube_link> <output_path>")
        sys.exit(0)

    link, output_path = sys.argv[1:3]
    download_from_link(link, output_path)
