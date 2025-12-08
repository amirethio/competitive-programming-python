# Problem: Arrival of the General
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/144/A
# Status: Solved 


# -------------------------------
# Approach:  
# 1. soldier_number accept and soldier_height
# 2.find max no and count the no of element before it = n make to front
# 3.find min no and count the no of element after it = m 
# 4. print => n+m
# -------------------------------

soldier_number = int(input())
soldier_height =  list(map(int , input().strip().split()))
max_h = max(soldier_height)
min_h = min(soldier_height)
n = soldier_height.index(max(soldier_height))
soldier_height.remove(max_h)
m =  soldier_height[::-1].index(min_h)
print(n+m)