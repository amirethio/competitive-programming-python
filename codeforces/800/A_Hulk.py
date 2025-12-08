# Problem:  Hulk
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/705/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. chate / love / hate layer 1, 2,3
# 2. accpt input feeling_layer
# 3. if lovelyer evenmultiply by string of "I hate that I love it"
# 4. else: even + i ahte it at last
# -------------------------------

feeling_layer = int(input())
feeling = "I hate that I love that "
hate = "I hate it"
both = "I hate that I love it"
if(feeling_layer == 1):
    print(hate)
else:
    if(feeling_layer%2 == 0):
        print((feeling_layer//2 -1 ) * feeling + both)
    else:
        print((((feeling_layer-1)//2) * feeling)+ hate)
  

