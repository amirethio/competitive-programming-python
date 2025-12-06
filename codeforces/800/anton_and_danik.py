# Problem: Anton and Danik
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/734/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept input total game_played and game_result
# 2. loop through game played and count anton 
# 3. danik =  game_played - anton
# 4. if denik > anton = > Danik else =>Anton = => Frenship
# ------------------------------

game_played =  int(input())
game_result = list(input().strip())
anton = 0
for i in range(game_played):
    if(game_result[i] == "A"):
        anton += 1
danki =  len(game_result) - anton
if(danki > anton):
    print("Danik")
elif(anton >  danki):
    print("Anton")
else:
    print("Friendship")

# NOTE : we can use .count("A") in here easily