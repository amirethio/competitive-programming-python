# Problem:  Stones on the Table
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/266/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept inputs which is stone_no and colos
# 2. declare a variable to hold previous color 
# 3. create new list if not prev and current are not equal
# -------------------------------

stone_no = int(input())
colors =  list(input().strip())
removing_color =  0
previous_color = colors[0]
for i in range(1 , len(colors)):
    if(previous_color == colors[i]):
        removing_color += 1
    else:
        previous_color = colors[i]
print(removing_color)



# 4
# BRBG