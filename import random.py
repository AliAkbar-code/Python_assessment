import random

# # All players
# All_Player_name = ("Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi", "Azam")
# length_of_all = len(All_Player_name)
# print(f"Total Players: {length_of_all}")

# # Add the 7th player to the main list (using tuple slicing and concatenation)
# Player_name = ("Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi")
# Player_name = Player_name + (All_Player_name[len(Player_name)],)  # Adding the 7th player

# print(f"Current Players: {Player_name}")

# # Generate random scores for each player (stored in a tuple)
# Score_Player = tuple(random.randint(30, 100) for _ in All_Player_name)

# # Show initial scores (for reference)
# print("\nInitial Random Scores:")
# for i in range(len(Player_name)):
#     print(f"{Player_name[i]}: {Score_Player[i]}")

# # User input: how many players are OUT
# out_players = int(input(f"\nEnter number of players OUT (0 to {len(Player_name)-2}): "))

# # Use tuple to get current batsmen indices
# current_batsmen_indices = (out_players, out_players + 1)

# # Set scores of players who haven't played yet to 0 (using tuple slicing)
# Score_Player = Score_Player[:out_players+2] + tuple(0 for _ in range(out_players + 2, len(Score_Player)))

# # Total score is the sum of current + out players
# all_score = sum(Score_Player)
# max_score = max(Score_Player[:out_players+2])  # among players who batted
# min_score = min(Score_Player[:out_players+2])  # among players who batted

# # Remaining players (not yet out)
# remaining_player = len(All_Player_name) - (out_players + 2)

# # Get current batsmen names and scores (from the tuple)
# current_batsman_1 = Player_name[current_batsmen_indices[0]]
# current_batsman_1_score = Score_Player[current_batsmen_indices[0]]

# current_batsman_2 = Player_name[current_batsmen_indices[1]]
# current_batsman_2_score = Score_Player[current_batsmen_indices[1]]

# # Print scoreboard
# print(f"""
# 🏏 PAKISTAN SCOREBOARD 🏏
# Total: {all_score}/{out_players}
# Currently Playing: 
#    - {current_batsman_1}: {current_batsman_1_score}
#    - {current_batsman_2}: {current_batsman_2_score}
# Highest Score So Far: {max_score}
# Lowest Score So Far: {min_score}
# Players Yet to Bat: {remaining_player}
# """) 

n=5

for i in range(1, n+1):
        print("*"*i)

for i in range(1,n+1):
      space = n-i
    
      print(' '* space + "*" *i)


for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

        
for i in range(n):
        print('*' * n)

for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))



