from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
minutes = yt.length/60
seconds = (minutes % 1) * 60
print("Length: %dm %ds" % (minutes ,seconds))
print("Views: ", yt.views)

#Can replace get_by_resolution() with get_highest_resolution()
yd = yt.streams.get_by_resolution(1080)

yd.download('/home/abefas/Downloads')

