# Created by SezerBozkir<admin@sezerbozkir.com> at 10/31/2019

from pytube import YouTube
from string import punctuation


def primitive_on_progress(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


def download_from_link(link, saving_path):
    yt = YouTube(link, on_progress_callback=primitive_on_progress)
    high_resolution = yt.streams.filter(progressive=True, subtype="mp4").order_by('resolution').desc().first()

    filename = "".join([x for x in map(lambda x: "_" if x in punctuation + " " else x, high_resolution.title)]).lower()
    saved_file_path = high_resolution.download(output_path=saving_path, filename=filename)
    return saved_file_path


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    # advanced progress bar taking from : https://stackoverflow.com/a/34325723
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def progress_function(self, stream, chunk, file_handle, bytes_remaining, video_filesize):
    size = video_filesize
    p = 0
    while p <= 100:
        progress = p
        print_progress_bar()
        p = percent(bytes_remaining, size)


def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc
