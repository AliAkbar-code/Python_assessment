import webbrowser
from meme.generator import generate_meme

meme = generate_meme()

print("Generated Meme:")
print("Caption:", meme["caption"])
print("Image URL:", meme["image_url"])

# Automatically open the image in the web browser
try:
    webbrowser.open(meme["image_url"])
except Exception as e:
    print("Could not open meme image:", e)
