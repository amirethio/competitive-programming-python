# Problem: Beautiful Matrix
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/263/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. 5 x 5 matrix
# 2. loop 5 times and find where x located row = i+1 and col= index +1
# 3. minimum move = (row , col) - (3,3)
# 4. print tee result
# -------------------------------


import math
for i in range(5):
    row  =  list(map(int , input().split()))
    if(1 in row):
        row_no=  i+1
        col_no = row.index(1)+1
row_move = math.fabs(row_no-3)
col_move = math.fabs(col_no -3)
print(int(row_move + col_move))


