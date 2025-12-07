# Problem: George and Accommodation
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/467/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept room_no aat line 1 and the next people_no and room capacity
# 2. create count var and loop room no times
# 3. increment when  capcity - people > 0  and print count 
# -------------------------------





room_no = int(input())
count=0
for i in range(room_no):
    people_no , room_capacity  = map(int , input().split())
    if(room_capacity- people_no >= 2):
        count += 1
print(count)
