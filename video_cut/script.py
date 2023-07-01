from moviepy.video.io.VideoFileClip import VideoFileClip

# Load the video file
video = VideoFileClip('input.mp4')

# Set the start and end times of the clip you want to extract (in seconds)
start_time = 5
end_time = 15

# Use the subclip method to extract the clip
clip = video.subclip(start_time, end_time)

# Save the extracted clip to a new video file
clip.write_videofile('output.mp4')
print('proccess is done!!!')
