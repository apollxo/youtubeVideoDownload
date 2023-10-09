from pytube import YouTube
import subprocess
import os

video = input('Enter Youtube Share Link\n')

yt = YouTube(video)

yt.title = 'input'

yt.streams.filter(adaptive=True)

video_stream = yt.streams.get_by_itag(18)
audio_stream = yt.streams.get_by_itag(250)
print('downloading video...')
video_stream.download()
print('downloading audio...')
audio_stream.download()
print('Merging audio and video...')

input_video = 'input.mp4'
input_audio = 'input.webm'
output = 'output.mp4'

command = [
	'ffmpeg',
	'-i', input_video,
	'-i', input_audio,
	'-c:V', 'copy',
	'-c:a', 'copy',
	output
]

with open("/dev/null", "w") as black_hole:
    subprocess.run(command, stdout=black_hole, stderr=black_hole, check=True)

print('deleting files...')
os.remove(input_video)
os.remove(input_audio)

print('Finished')



# from pytube import YouTube
# import subprocess
# import os

# video = input('Enter Youtube Share Link\n')

# yt = YouTube(video)

# yt.title = 'input'

# yt.streams.filter(adaptive=True)

# video_stream = yt.streams.get_by_itag(18)
# audio_stream = yt.streams.get_by_itag(250)
# print('downloading video...')
# video_stream.download()
# print('downloading audio...')
# audio_stream.download()
# print('Merging audio and video...')

# input_video = 'input.mp4'
# input_audio = 'input.webm'
# output = 'output.mp4'

# command = [
# 	'ffmpeg',
# 	'-i', input_video,
# 	'-i', input_audio,
# 	'-c:V', 'copy',
# 	'-c:a', 'copy',
# 	output
# ]

# with open("/dev/null", "w") as black_hole:
#     subprocess.run(command, stdout=black_hole, stderr=black_hole, check=True)

# print('deleting files...')
# os.remove(input_video)
# os.remove(input_audio)

# print('Finished')



