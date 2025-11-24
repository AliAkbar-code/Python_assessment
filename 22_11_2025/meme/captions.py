import random

def get_random_caption():
    try:
        captions = [
            "When you realize it's Monday again...",
            "Me trying to act normal after 3 cups of coffee.",
            "That moment when your code finally works!",
            "When WiFi connects automatically 😎",
            "Me: I'll sleep early today. Also me at 3 AM: 😂"
        ]

        if not captions:
            raise ValueError("Caption list is empty.")

        return random.choice(captions)

    except Exception as e:
        print("Error getting caption:", str(e))
        return "No caption available 😢"
