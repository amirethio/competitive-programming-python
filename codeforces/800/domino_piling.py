# Problem: Domino piling
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/50/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. M x N Board  and  domino 2 x 1  square 
# 2.accept the input which are  m and N
# 3.max_dominotes =  area // 2
# -------------------------------



n , m =  map(int , input().split())
area =  n * m
max_dominoes =  area // 2
print(max_dominoes)


