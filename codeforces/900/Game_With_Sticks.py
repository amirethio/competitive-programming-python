# Problem: Game With Sticks
# Difficulty: 900
# Link: https://codeforces.com/problemset/problem/451/A
# Status: Solved 


# -------------------------------
# Approach:
# - finding the one with nth to move 
# 1. accept n and n to form to grid 
# 2. find the minimum of n and m
# 3. if even print Malvika
# 4. else  Akshat




[n , m ] = list(map(int,input().split()))
number  = min(n , m)
 
if(number%2 == 0):
	print('Malvika' )
else:
	print('Akshat')
    





