from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Load video
video_clip = VideoFileClip(r'C:\Users\smuku\DjangoProject\Y22MLOPS\MyGit\Earth.mp4')

# Load image to overlay (correct the path)
image_clip = ImageClip(r'C:\Users\smuku\DjangoProject\Y22MLOPS\MyGit\sac.png')

# Set the duration of the image overlay (same as video duration)
image_clip = image_clip.set_duration(video_clip.duration)

# Resize the image (optional)
image_clip = image_clip.resize(height=100)  # Resize to desired height
image_clip = image_clip.set_position(("right", "top"))  # Set position (e.g., top-right corner)

# Overlay the image on the video
composite_clip = CompositeVideoClip([video_clip, image_clip])

# Write the output video
composite_clip.write_videofile("output_video_with_overlay.mp4", codec="libx264")
