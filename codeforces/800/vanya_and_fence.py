# Problem: Beautiful Matrix
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/263/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accpt the people_no and fence_height also heigs of no
# 2. count thise which are taller tahn fence  //looping
# 3. minimum possible width =  taller = people-No
# 4. print minimum possible 
# -------------------------------

people_no , fence_height =  map(int , input().split())
height =   list(map(int , input().split()))
taller_no = 0
for i in height:
    if(i > fence_height):
        taller_no +=1
print(people_no + taller_no)
