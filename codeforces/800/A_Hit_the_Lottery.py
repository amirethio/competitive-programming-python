# Problem: Hit the Lottery
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/996/A
# Status: Solved 


# -------------------------------
# Approach:  
# 1. accept bank_dollar
# 2.  in 5 if cases count in each using //
# 3. print count
# -------------------------------

bank_dollar =  int(input())
count = 0
bills  = [100,20,10,5,1]
for i in range(5):
    if(bank_dollar //bills[i] > 0):
        count += bank_dollar //bills[i]
        bank_dollar -= bills[i] *(bank_dollar //bills[i])
print(count)