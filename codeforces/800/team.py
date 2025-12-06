# Problem: Tram
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/116/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. n = stop_no 
# 2. loop stop_no times and on each loop and accept leave inter
# 3. max_hold on each loop is previos + (inter-leave)
# 4. print the max of mac hold 
# -------------------------------


stop_no =  int(input())

max_holds = []
previos = 0 ;
for i in range(stop_no):
    exit, inter  = map(int , input().split())
    current = (inter-exit)+previos
    max_holds.append(current)
    previos =  current;
print(max(max_holds))
