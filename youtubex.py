# Created by SezerBozkir <admin@sezerbozkir.com> at 10/31/2019


import sys
import os
from utils import download_from_link

if __name__ == '__main__':
    if os.name == "nt":
        saving_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        link = input("Please enter youtube link?")
        output_path = input("Please enter output path?")
        proxy = input("Please enter proxy address?(optional) (http://proxy:port)")
        proxy = {"http": proxy} if proxy else None
    else:
        saving_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        if len(sys.argv) != 3:
            print(
                "Using: python youtubex.py <youtube_link> <output_path> <proxy_address(optional)>")
            sys.exit(0)
        link, output_path = sys.argv[1:3]
        try:
            proxy = {"http": sys.argv[3]}
        except IndexError:
            proxy = None
    # sample link = https://www.youtube.com/watch?v=xWOoBJUqlbI
    # sample path = C:\Users\<user_name>\Desktop
    download_from_link(link, output_path, proxy)
