# Problem: Twins
# Difficulty: 900
# Link: https://codeforces.com/problemset/problem/160/A
# Status: Solved 


# -------------------------------
# Approach:
# - find min no of coins to  make it stictly greater than 
# 1. accptpt n no of coins
# 2. 2nd line accpt coins    
# 3. sort the array and find the strict greater than
# 4. whe u find print the no and break


n = int(input())
coins = sorted(list(map(int, input().split())))
for i in range( -1 , -(len(coins)+1) , -1 ,):
    if(sum(coins[:i]) < sum(coins[i:])):
        print(abs(i))
        break







