import random

def get_random_image_url():
    try:
        images = [
            "https://i.imgflip.com/30b1gx.jpg",   # Distracted Boyfriend
            "https://i.imgflip.com/26am.jpg",     # Grumpy Cat
            "https://i.imgflip.com/2/4t0m5.jpg",  # Drake Hotline Bling
            "https://i.imgflip.com/9ehk.jpg",     # Success Kid
            "https://i.imgflip.com/1otk96.jpg",   # Confused Nick Young
            "https://i.imgflip.com/3lmzyx.jpg",   # Woman Yelling at Cat
            "https://i.imgflip.com/5kdc.jpg",     # Ancient Aliens
            "https://i.imgflip.com/2wifvo.jpg"    # Pikachu Surprise
        ]

        if not images:
            raise ValueError("Image URL list is empty.")

        return random.choice(images)

    except Exception as e:
        print("Error getting image URL:", str(e))
        return "https://via.placeholder.com/300x200?text=Error"
