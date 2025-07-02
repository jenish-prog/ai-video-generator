import re

def split_text_into_scenes(script):
    scenes = re.split(r'(?<=[.!?])\s+', script.strip())
    return scenes
