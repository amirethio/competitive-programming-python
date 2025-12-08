# Problem: I Wanna Be the Guy
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/469/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accpt max_level on 1st line  and next 2 lines put on same set called levels
# 2. and if len of levels  ==  acceptmax then its pass
# 3.if pass print I become the guy.
# 4. else: => Oh, my keyboard!
# -------------------------------

max_level = int(input())
level = []
data_one = input().split()
data_two = input().split()
level.extend(data_one[1:])
level.extend(data_two[1:])
level =  set(level)
if("0" in level):
    level.remove("0")
if(len(level) == max_level):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")