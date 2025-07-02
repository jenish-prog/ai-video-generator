from PIL import Image

def generate_image(scene_text, index):
    img = Image.new('RGB', (1280, 720), color=(73, 109, 137))
    img.save(f"assets/images/scene_{index}.png")
