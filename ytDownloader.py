from pytube import YouTube
from sys import argv

#Change this
path = '/home/user/Downloads'

def print_manual():
    print('\n' + '\033[1m' + 'NAME' + '\033[0m')
    print("\tytDownloader - A python script to download video/audio from YouTube")
    print('\n' + '\033[1m' + 'SYNOPSIS' + '\033[0m')
    print("\tytDownloader.py <YouTube link> [options]")
    print('\n' + '\033[1m' + 'OPTIONS' + '\033[0m')
    print("\n\033[1m\tNO OPTION\033[0m\n\t\tDownload the video in 1080p")
    print("\n\033[1m\t-a\033[0m\n\t\tChoose to download from all available audio streams")
    print("\n\033[1m\t--mp4\033[0m\n\t\tChoose to download from all available mp4 streams")
    print("\n\033[1m\t-h\033[0m\n\t\tDownload stream with the highest resolution")
    print("\n\033[1m\t--720p\033[0m\n\t\tDownload stream with 720p resolution")
    print("\n\033[1m\t--480p\033[0m\n\t\tDownload stream with 480p resolution")
    print("\n\033[1m\t-la\033[0m\n\t\tChoose to download from all available streams\n")
    exit(0)


if len(argv) < 2:
    print_manual()

link = argv[1]
yt = YouTube(link)

if len(argv) == 3:
    arg2 = argv[2]
else:
    arg2 = None

#Display some info
print("Title: ", yt.title)
minutes = yt.length/60
seconds = (minutes % 1) * 60
print("Length: %dm %ds" % (minutes ,seconds))
print("Views: ", yt.views)


if arg2 == None:
    stream = yt.streams.get_by_resolution(1080)
    stream.download(path)
elif arg2 == "-a":
    print(yt.streams.filter(only_audio=True))
    itag = input("Choose itag to download: ")
    stream = yt.streams.get_by_itag(itag)
    stream.download(path) 
elif arg2 == "--mp4":
    print(yt.streams.filter(file_extension='mp4'))
    itag = input("Choose itag to download: ")
    stream = yt.streams.get_by_itag(itag)
    stream.download(path) 
elif arg2 == "-h":
    stream = yt.streams.get_highest_resolution()
    stream.download(path)
elif arg2 == "--720p":
    stream = yt.streams.get_by_resolution(720)
    stream.download(path)
elif arg2 == "--480p":
    stream = yt.streams.get_by_resolution(480)
    stream.download(path)
elif arg2 == "-la":
    print(yt.streams.filter(adaptive=True))
    itag = input("Choose itag to download: ")
    stream = yt.streams.get_by_itag(itag)
    stream.download(path) 
else:
    print_manual() 

                  


