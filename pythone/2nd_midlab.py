def main():
    print("🐒 Welcome to the Epic Jungle Trip Mad Libs! 🐒")
    print("Fill in the blanks with your own words and create a funny jungle adventure.\n")

    # Collect inputs
    friend_name = input("Enter your best friend's name: ")
    your_name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter a city: ")
    food = input("Enter a food you love: ")
    fruit = input("Enter a fruit: ")
    tree = input("Enter a type of tree: ")
    animal_noise = input("Enter a funny animal noise: ")
    verb_ing = input("Enter a verb ending in -ing (e.g., running): ")
    drink = input("Enter a drink: ")
    sticky_thing = input("Enter something sticky: ")
    backpack_item = input("Enter something you might find in a backpack: ")

    # Print the story with the inputs
    story = f"""
Last summer, my loyal best friend {friend_name} and I ({your_name}), both aged {age}, decided to become jungle explorers near {city}.  
We packed our bags full of {food}, cameras, and so much confidence it felt like the jungle was our personal playground — which we soon regretted!

The jungle was so thick with tall {tree} trees, and everywhere weird sounds like "{animal_noise}!" echoed, along with mysterious rustling that made us feel like someone was secretly eavesdropping on us.  
Suddenly, a mischievous monkey appeared and said, "Hey folks! These friends are my new best buddies!"

First, it stole {friend_name}’s hat and climbed up a {tree} tree like some ninja monkey master!  
Then it jumped onto my backpack looking for my secret stash of {fruit}.  
Before we could stop it, the monkey grabbed my {drink} and shook it like a soda can, splashing {sticky_thing} all over both of us like we’d turned into sticky lizards!

We chased the monkey, slipping on roots, falling into bushes, and breaking a few plants ourselves, while it swung from vines making noises like it was hosting a monkey rock concert.  
At one point, it even grabbed my {backpack_item} and tried to eat it, probably thinking it was a tasty chocolate!

Finally, when we scared it away with a bunch of bananas, we were dirty, sweaty, and laughing so hard that even the jungle’s breeze stopped to watch.  
We didn’t find any hidden treasure that day — but we found a monkey who thinks it’s the king of the jungle… and the ultimate prankster!

Moral of the story:  
A jungle monkey isn’t your friend — it’s your clever little prankster brother!  
Never trust it with your stuff or your snacks, or you’ll end up covered in {sticky_thing}!
"""

    print("\n📝 Here’s your Epic Jungle Trip story:\n")
    print(story)

if __name__ == "__main__":
    main()
