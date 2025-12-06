# Problem: Translation
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/41/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept input Berlandish(s) and Birlandish(t)
# 2. reverse the Birlandish(t)
# 3. if s == t => YES else => NO
# ------------------------------

s_berlandish =  input().strip()
t_birlandish =  input().strip()[::-1]
if(s_berlandish == t_birlandish):
    print("YES")
else:
    print("NO")