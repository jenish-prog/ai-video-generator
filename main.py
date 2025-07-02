from src.text_to_scenes import split_text_into_scenes
from src.image_generator import generate_image
from src.voice_generator import generate_voiceover
from src.subtitle_generator import generate_srt
from src.video_editor import create_video

if __name__ == "__main__":
    script = "A boy walks into a forest. He sees a glowing butterfly. Suddenly, it flies into the sky."
    scenes = split_text_into_scenes(script)

    for i, scene in enumerate(scenes):
        generate_image(scene, i)

    generate_voiceover(scenes)
    generate_srt(scenes, [4]*len(scenes))
    create_video(len(scenes))
