def main():
    print("🎪 Welcome to the Circus Chaos Mad Libs Game! 🎪")
    print("Fill in the blanks below to create your own funny circus story.\n")

    # Collect user input
    friend1 = input("Enter Friend’s Name 1: ")
    friend2 = input("Enter Friend’s Name 2: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    fruit = input("Enter a Fruit: ")
    adjective = input("Enter an Adjective: ")
    object_ = input("Enter a Random Object: ")
    verb_ing = input("Enter a Funny Verb ending in -ing: ")
    loud_word = input("Enter Something Loud You Yell: ")
    costume = input("Enter a Costume: ")
    animal = input("Enter an Animal: ")
    food = input("Enter a Food: ")
    magic_word = input("Enter a Magic Word: ")

    # Story using f-string
    story = f"""
Last weekend in {city}, two best friends — {friend1} and {friend2}, both aged {age} — decided to go to the circus 
because they heard there was free {fruit}. As soon as they arrived, {friend2} caused a scene by showing up in a 
full {costume} costume and tripping over a {object_} right at the entrance. The clown laughed so hard he nearly fell off his unicycle.

Inside the tent, things got even crazier. During the lion show, {friend1} leaned over and whispered, 
“What if the {animal} forgets it's trained?” Two seconds later, the lion roared, and {friend2} screamed, 
“{loud_word}!” and tried {verb_ing} out of the exit while spilling popcorn all over a kid. 
Later, the magician called {friend1} on stage and shouted “{magic_word}” — but instead of disappearing, 
{friend1} sneezed and knocked over the magician’s table, launching a plate of {food} into the crowd.

🎯 Moral of the story:
Never go to the circus with your best friend. Especially if they dress like a {costume} and think lions are just big kittens.
    """

    print("\n📝 Here's your story:")
    print(story)


if __name__ == "__main__":
    main()
