# Problem: Drinks
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/200/B
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept o_conta_numbe and percent_drinks
# 2. add up drinks and divinde by 100 times of continer 
# 3. then multiply by 100
# 4. print result 
# -------------------------------

# even it's error the problem consider errors in some range

container =  int(input())
drinks =  list(map(int , input().split()))
result =  (sum(drinks)/100)/container
print(result*100)