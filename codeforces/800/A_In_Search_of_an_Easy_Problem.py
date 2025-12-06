# Problem: In Search of an Easy Problem
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/1030/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. 1 hard => chnage problem
# 2. accept asked_people  and  question_status 
# 3. if 1 in question_status = > HARD  : => EASY
# -------------------------------



asked_people = int(input())
question_status = list(map(int , input().strip().split()))
if(1 in question_status):
    print("HARD")
else:
    print("EASY")

