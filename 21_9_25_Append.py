# list1 = ["advance Pythong","Machine Learning","Natural Processing"]
# # list2 = ["Artifical Intelligence","javaSript","Node"]
# list1.append("Artifical Intelligence")
# list1.append("JavaScript")
# list1.append("Node")
# print(list1)

# Player_name = ["Babar","Shaheen","Fakhar","salman","Agha"]
# Score_Player=[34,54,56,34,35]
# Player_name.insert(1,"Fakher Zaman")
# print(Player_name)
# new_player= ["salman","Agha"]
# new_player_score=[34,35]
# print(new_player_score)

# Player_name.extend(new_player)
# Score_Player.extend(new_player_score)
# print(Score_Player)
# print(Player_name)
# Player_name.extend(Score_Player)
# print(Player_name)
# import random
# All_Player_name = ["Babar","Shaheen","Fakhar","salman","Agha","Afridi","Azam"]
# length_of_all=len(All_Player_name)
# print(length_of_all)
# Player_name = ["Babar","Shaheen","Fakhar","salman","Agha","Afridi"]
# Player_name.append(All_Player_name[len(Player_name)])
# print(Player_name)
# Score_Player=[random.randint(30, 100) for _ in Player_name] 
# print(Score_Player)
# all_score=sum(Score_Player)
# max_score=max(Score_Player)
# min_score=min(Score_Player)
# # print(all_score)

# remaining_player=len(Player_name)-3
# # print(remaining_player)

# five_player=Player_name[4]
# five_player_score=Score_Player[4]
# # print(five_player,five_player_score)

# six_player = Player_name[5]
# six_player_score = Score_Player[5]

# print(f"""
# PAKISTAN {all_score}/{remaining_player} : {five_player}/{five_player_score}   {six_player}/{six_player_score}\n{five_player} have maximum Score Of Player {max_score}\n{Player_name[0]} have minimum score {min_score}

# """)

# add name of list player name score and of cricket team player to score of player and find the total score heighest score by player and how many player out and kust like the board on tv


# again

# import random

# All_Player_name = ["Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi", "Azam"]
# length_of_all = len(All_Player_name)
# print(length_of_all)



# Player_name = ["Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi"]
# Player_name.append(All_Player_name[len(Player_name)])
# print(Player_name)

# # Generating random scores for players
# Score_Player = [random.randint(30, 100) for _ in All_Player_name] 

# user_value = 4
# Score_Player[user_value+2:] = [0]*(len(Score_Player)-user_value-2)


# print(Score_Player)
#  # Random score between 30 and 100 for each player
# all_score = sum(Score_Player)
# max_score = max(Score_Player)
# min_score = min(Score_Player)

# remaining_player = len(Player_name) - user_value

# five_player = Player_name[4]
# five_player_score = Score_Player[4]

# six_player = Player_name[5]
# six_player_score = Score_Player[5]

# print(f"""
# PAKISTAN {all_score}/{remaining_player} : {five_player}/{five_player_score}   {six_player}/{six_player_score}

# """)

# {five_player} has maximum Score Of Player {max_score}
# {Player_name[0]} has minimum score {min_score}


# again 2
# l=[7,4,5]
# l1 =[4,7,8]
# l=l1[:]
# print(id(l[2]),id(l1[2]))
# l=[4,5,6,7,3,2,1] 
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

# import random

# # All players
# All_Player_name = ["Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi", "Azam"]
# length_of_all = len(All_Player_name)
# print(f"Total Players: {length_of_all}")

# # Add the 7th player to the main list
# Player_name = ["Babar", "Shaheen", "Fakhar", "salman", "Agha", "Afridi"]
# Player_name.append(All_Player_name[len(Player_name)])
# print(f"Current Players: {Player_name}")

# # Generate random scores for each player
# Score_Player = [random.randint(30, 100) for _ in All_Player_name]
# # Show initial scores (for reference)
# print("\nInitial Random Scores:")
# for i in range(len(Player_name)):
#     print(f"{Player_name[i]}: {Score_Player[i]}")
# # User input: how many players are OUT
# out_players = int(input(f"\nEnter number of players OUT (0 to {len(Player_name)-2}): "))

# # Calculate who is currently playing
# current_batsmen_indices = [out_players, out_players + 1]

# # Set scores of players who haven't played yet to 0
# for i in range(out_players + 2, len(Score_Player)):
#     Score_Player[i] = 0

# # Total score is the sum of current + out players
# all_score = sum(Score_Player)
# max_score = max(Score_Player[:out_players+2])  # among players who batted
# min_score = min(Score_Player[:out_players+2])  # among players who batted

# # Remaining players (not yet out)
# remaining_player = len(All_Player_name) - (out_players + 2)

# # Get current batsmen names and scores
# current_batsman_1 = Player_name[current_batsmen_indices[0]]
# current_batsman_1_score = Score_Player[current_batsmen_indices[0]]

# current_batsman_2 = Player_name[current_batsmen_indices[1]]
# current_batsman_2_score = Score_Player[current_batsmen_indices[1]]

# # Print scoreboard
# print(f"""
# 🏏 PAKISTAN SCOREBOARD 🏏
# Total: {all_score}/{out_players}
# Currently Playing: 
#   - {current_batsman_1}: {current_batsman_1_score}
#   - {current_batsman_2}: {current_batsman_2_score}
# Highest Score So Far: {max_score}
# Lowest Score So Far: {min_score}
# Players Yet to Bat: {remaining_player}
# """)

# import platform
# import os
# import sys

# print("=== Basic OS Info ===")
# print(f"Platform Identifier: {sys.platform}")
# print(f"System: {platform.system()}")
# print(f"Node Name (Hostname): {platform.node()}")
# print(f"Release: {platform.release()}")
# print(f"Version: {platform.version()}")
# print(f"Machine: {platform.machine()}")
# print(f"Processor: {platform.processor()}")

# print("\n=== More Detailed Info ===")
# print(f"Platform: {platform.platform()}")
# print(f"Architecture: {platform.architecture()}")

# # If available, use uname for even more info
# try:
#     print("\n=== Uname Info ===")
#     uname_info = os.uname()
#     print(f"Sysname: {uname_info.sysname}")
#     print(f"Nodename: {uname_info.nodename}")
#     print(f"Release: {uname_info.release}")
#     print(f"Version: {uname_info.version}")
#     print(f"Machine: {uname_info.machine}")
# except AttributeError:
#     print("\nos.uname() not available on this OS (usually only on Unix-like systems).")

t=(67,30,34,[34,32,35])
t[3].append(8)
print(t)
a=(8,8,9)
b=(5,4,3)
b=list(b)
print(type(b))