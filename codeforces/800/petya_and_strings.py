# Problem: Petya and Strings
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/112/A
# Status: Solved 


# -------------------------------
# Approach:
# 1.  first 2 lines compaired values
# 2. chnage both of them in to capital  or small
# 3. compair the above chnaged strings
# 4. if first_str < sec_str => -1 :equal = 0 : else:1
# -------------------------------



first_str =  input().lower()
second_str =  input().lower()
if(first_str < second_str):
    print(-1)
elif(first_str > second_str):
    print(1)
else:
    print(0)

# NOTE: use .strip incase if there are any  incomping spaces that's recommended