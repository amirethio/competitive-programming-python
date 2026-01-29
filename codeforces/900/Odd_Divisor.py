# Problem: Odd Divisor
# Difficulty: 900
# Link:https://codeforces.com/problemset/problem/1475/A
# Status: Solved 


# -------------------------------
# Approach:
# - checking if it has odd divisor
# 1. accptpt n no of test cases
# 2. loop n timesand accpt test cases
# 3. inisde loop if no is odd print => YES
# 4. if not check if its divisble by odd nos


n = int(input())
for i in range(n):
    num = int(input())
    # removing all odd divisor
    while num%2 == 0:
        num = num // 2
    if(num >1 ):
        print("YES")
    else:
        print("NO")

# *NOTE:
# . 







