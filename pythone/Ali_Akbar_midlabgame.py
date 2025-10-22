print("Please enter the following details for your jungle story:\n")

friend_name = input("Friend's name: ").strip()
your_name = input("Your name: ").strip()
age = input("Age: ").strip()
city = input("City: ").strip()
animal = input("animal: ").strip()
food = input("Food (plural): ").strip()
tree = input("Type of tree: ").strip()
animal_noise = input("Animal noise: ").strip()
drink = input("Drink: ").strip()
backpack_item = input("Backpack item: ").strip()
sticky_thing = input("Sticky thing (like honey or jam): ").strip()

story = f"""
Last summer, my loyal best friend {friend_name} and I ({your_name}), both aged {age}, decided to explore the jungle near {city}.  
We packed our bags full of {food}, cameras, and enough confidence to think the jungle was our personal playground — which we soon regretted!

The jungle was thick with tall {tree} trees, and everywhere weird sounds like "{animal_noise}!" echoed, making us feel like we were being secretly watched.  
Suddenly, a mischievous {animal} appeared and said, "Hey folks! These friends are my new best buddies!"

First, it stole {friend_name}’s hat and climbed up a {tree} tree like some ninja monkey master!  
Then it jumped onto my backpack looking for my secret stash of {food}.  
Before we could stop it, the {animal} grabbed my {drink} and shook it like a soda can, splashing {sticky_thing} all over both of us like we’d turned into sticky lizards!

We chased the {animal}, slipping on roots, falling into bushes, and breaking a few plants ourselves, while it swung from vines making noises like it was hosting a {animal} rock concert.  
At one point, it even grabbed my {backpack_item} and tried to eat it, probably thinking it was a tasty chocolate!

Finally, when we scared it away with a bunch of bananas, we were dirty, sweaty, and laughing so hard that even the jungle’s breeze stopped to watch.  
We didn’t find any hidden treasure that day — but we found a {animal} who thinks it’s the king of the jungle… and the ultimate prankster!

Moral of the story:  
A jungle {animal} isn’t your friend — it’s your clever little prankster brother!  
Never trust it with your stuff or your snacks, or you’ll end up covered in {sticky_thing}!
"""

print(story)
