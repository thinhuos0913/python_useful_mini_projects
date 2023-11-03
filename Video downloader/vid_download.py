from pytube import YouTube
from sys import argv

link = argv[1]
# link = 'https://www.youtube.com/watch?v=bzxpjra25zc'
yt = YouTube(link)

print('Title:', yt.title)
print('Views:', yt.views)


yd = yt.streams.get_highest_resolution()
yd.download('./download_video')

