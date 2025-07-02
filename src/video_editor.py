from moviepy.editor import *

def create_video(num_scenes, duration=4):
    clips = []
    for i in range(num_scenes):
        img = ImageClip(f"assets/images/scene_{i}.png").set_duration(duration).resize(height=720)
        audio = AudioFileClip(f"assets/audio/voice_{i}.mp3")
        img = img.set_audio(audio)
        clips.append(img)
    final = concatenate_videoclips(clips)
    final.write_videofile("assets/video/ai_video_output.mp4", fps=24)
