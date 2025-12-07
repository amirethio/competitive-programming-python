# Problem: Magnets
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/344/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept magnet_number
# 2. loop magnet no times  and accept poles
# 3. declare count var to count the index
# 4.Print result 
# -------------------------------


magnet_number = int(input())
count = 1
poles = []
for i in range(magnet_number):
    poles.append(input().strip())
for i in range(magnet_number-1):
    if(poles[i] != poles[i+1]):
        count += 1
print(count)


# inhere we can accept the fist value on ple and use only 1 loop