from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Title", yt.title)
print("Views", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:\EDIT VIDEO WITH EMMAN\TEST TASK')

#HOW TO USE
#python -u YTdownloader.py "link"
#example ->
#python -u YTdownloader.py "https://www.youtube.com/watch?v=3sCGysVB41k"