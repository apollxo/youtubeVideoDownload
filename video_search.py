import urllib.request
import re

ask = input('Enter youtube video name: \n')
newStr = ask.replace(' ', '+')
html = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={newStr}')
video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())

ids = list(set(video_ids))
#print(ids)
for i in range(len(ids)):
	print('https://www.youtube.com/watch?v=' + ids[i]) 

