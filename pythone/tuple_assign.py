
# profile = ("Beth", ["Math"], 200)

# # Unpack
# name, category_list, score = profile

# # Convert list to string
# category_str = ", ".join(category_list)
# print(type(name))
# print(type(category_str))
# print(type(score))

# print(f"Name: {name}, Category: {category_str}, Score: {score}")


# 2nd------------------------------------------------


# prize = ("Trip", 100, ["Europe"])


# name, amount, location = prize
# print(type(amount))

# amount = str(amount)
# print(type(amount))

# is_valid = "Valid" if len(amount) == 3 else "Invalid"



# print(f" Status: {is_valid}")

# 3-----------------------------------------------------

# Given
# contestant = ("Cody", [], 0)

# # Unpack
# name, answer_list, points = contestant
# print(type(points))
# print(type(name))
# print(type(answer_list))
# # Ensure points is int
# points = int(points)

# # Rule: if points is zero → add 10
# if points == 0:
#     points += 10

# # Output
# print(f"Updated Points: {points}")

# 4--------------------------------------------------------------

# import random


# all_players = ("Babar Azam", "Fakhar Zaman", "Imam-ul-Haq", "Mohammad Rizwan",
#                "Iftikhar Ahmed", "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah")   # tuple now


# players_out = 6


# currently_playing = 2

# played_count = players_out + currently_playing
# print(played_count)


# played_scores = [random.randint(10, 100) for _ in range(played_count)]
# print(played_scores)


# remaining_players = len(all_players) - played_count
# not_played_scores = [0] * remaining_players


# score_of_players = tuple(played_scores + not_played_scores)

# total_score = sum(played_scores)
# highest_score = max(played_scores)

# current_batsman_1 = all_players[players_out]
# current_batsman_1_score = score_of_players[players_out]

# current_batsman_2 = all_players[players_out + 1]
# current_batsman_2_score = score_of_players[players_out + 1]


# print("\n  LIVE CRICKET SCOREBOARD  ")
# print(f"Total Score       : {total_score}/{players_out}    {current_batsman_1:<15} - {current_batsman_1_score}   {current_batsman_2:<15} - {current_batsman_2_score} ")
# print(f"Currently Playing")
# print(f"Highest Score So Far   : {highest_score} runs")
# print(f"Players Yet to Bat     : {remaining_players}") 


# We use a tuple because it is immutable, 
# meaning data like player names or fixed scores
#  cannot be accidentally changed. 
# It also improves performance and memory efficiency,
#  and clearly shows the data is read-only