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

# from moviepy.video.io.VideoFileClip import VideoFileClip

# # Load the video file
# video = VideoFileClip('input.mp4')

# # Set the start and end times of the clip you want to extract (in seconds)
# start_time = 5
# end_time = 15

# # Use the subclip method to extract the clip
# clip = video.subclip(start_time, end_time)

# # Save the extracted clip to a new video file
# clip.write_videofile('output.mp4')
# print('proccess is done!!!')
