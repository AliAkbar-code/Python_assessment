# # task 1 book
# book = [
#     ["Page 1: Introduction", [
#         "This is the first page.",
#         "It introduces the story.",
#         "Dummy line for page 1."
#     ]],

#     ["Page 2: Characters", [
#         "This page lists characters.",
#         "Hero: Alex",
#         "Villain: Shadow"
#     ]],

#     ["Page 3: Journey", [
#         "The adventure begins here.",
#         "They face challenges.",
#         "Dummy line for page 3."
#     ]],

#     ["Page 4: Climax", [
#         "The big fight happens.",
#         "A twist is revealed.",
#         "Dummy line for page 4."
#     ]],

#     ["Page 5: Conclusion", [
#         "Story comes to an end.",
#         "Moral: Stay strong.",
#         "Dummy line for page 5."
#     ]]
# ]

# page1 = book[0]
# page2 = book[1]
# page3 = book[2]
# page4 = book[3]
# page5 = book[4]


# print(page3[0])       
# print(page3[1][0])    
# print(page3[1][1])    
# print(page3[1][2])    

# # task for show cricket team score 


# import random

# # All players in batting order
# all_players = ["Babar Azam", "Fakhar Zaman", "Imam-ul-Haq", "Mohammad Rizwan",
#                "Iftikhar Ahmed", "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah"]

# # out player 
# players_out = 2

# # Total players 
# currently_playing = 2

# # Total players who played
# played_count = players_out + currently_playing
# print(played_count)
# played_scores = [random.randint(10, 100) for _ in range(played_count)]
# print(played_scores)

# # Assign 0 to players who have not batted yet
# remaining_players = len(all_players) - played_count
# not_played_scores = [0] * remaining_players

# # Combine all scores in order
# score_of_players = played_scores + not_played_scores


# total_score = sum(played_scores)
# highest_score = max(played_scores)


# current_batsman_1 = all_players[players_out]
# current_batsman_1_score = score_of_players[players_out]

# current_batsman_2 = all_players[players_out + 1]
# current_batsman_2_score = score_of_players[players_out + 1]

# # Display the scoreboard
# print("\n  LIVE CRICKET SCOREBOARD  ")
# print(f"Total Score       : {total_score}/{players_out}    {current_batsman_1:<15} - {current_batsman_1_score}   {current_batsman_2:<15} - {current_batsman_2_score} ")
# print(f"Currently Playing")
# print(f"Highest Score So Far   : {highest_score} runs")
# print(f"Players Yet to Bat     : {remaining_players}")
 


import random

# All players in batting order
all_players = ["Babar Azam", "Fakhar Zaman", "Imam-ul-Haq", "Mohammad Rizwan",
               "Iftikhar Ahmed", "Shadab Khan", "Shaheen Afridi", "Haris Rauf", "Naseem Shah"]

players_out = 6      # players already out
currently_playing = 2     # currently batting
played_count = players_out + currently_playing

# Scores for played batsmen
played_scores = [random.randint(10, 100) for _ in range(played_count)]

# Scores for those yet to bat
not_played_scores = [0] * (len(all_players) - played_count)

# Final score list in batting order
score_of_players = played_scores + not_played_scores

# Total and highest score
total_score = sum(played_scores)
highest_score = max(played_scores)


status_list = (["OUT"] * players_out +
               ["NOT OUT *"] * currently_playing +
               ["Yet to Bat"] * (len(all_players) - played_count))


print("         LIVE CRICKET SCORECARD     ")


print(f"Total Score: {total_score}/{players_out}\n")

print("Batting Card:")
for player, score, status in zip(all_players, score_of_players, status_list):
    print(f"  {player:<15} {score:>3}  {status}")


print(f"Highest Score So Far : {highest_score} runs")
print(f"Players Yet to Bat   : {len(all_players) - played_count}") 

