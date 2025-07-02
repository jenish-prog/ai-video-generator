import pyttsx3

def generate_voiceover(scene_texts):
    engine = pyttsx3.init()
    for i, text in enumerate(scene_texts):
        engine.save_to_file(text, f"assets/audio/voice_{i}.mp3")
    engine.runAndWait()

