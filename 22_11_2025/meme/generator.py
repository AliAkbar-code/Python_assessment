from .captions import get_random_caption
from .images import get_random_image_url

def generate_meme():
    try:
        caption = get_random_caption()
        image_url = get_random_image_url()

        if caption is None or image_url is None:
            raise ValueError("Caption or image URL could not be generated.")

        meme = {
            "caption": caption,
            "image_url": image_url
        }

        return meme

    except Exception as e:
        print("Error generating meme:", str(e))
        return {
            "caption": "Error creating meme 😢",
            "image_url": "https://via.placeholder.com/300x200?text=Error"
        }
