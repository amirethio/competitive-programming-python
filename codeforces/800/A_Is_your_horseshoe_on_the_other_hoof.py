# Problem:  Is your horseshoe on the other hoof?
# Difficulty: 1000
# Link: https://codeforces.com/problemset/problem/228/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. aceept input which is color_owned
# 2. put the color woned on set and it name color
# 3. print 4 -  color
# -------------------------------


color_owned = set(input().split())
print(4 - len(color_owned))