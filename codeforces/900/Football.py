# Problem: Football
# Difficulty: 900
# Link: https://codeforces.com/problemset/problem/96/A
# Status: Solved 


# -------------------------------
# Approach:
# -  to determine if the arrangement is dangerous or not 
# 1. accept the arrangement (arrange)
# 2. the use to pointer  to track if there is consequative 7 0's or 1'a untilthe last one    
# 3. if u find the consequative print Yes and break
# 4. else print NO


arrange = list(map(int , list(input())))
answer = "NO"


for i in range(0,len(arrange)-6):
    if(len(arrange) < 7):
        print("here")
        break
    elif(sum(arrange[i:i+7]) == 0 or sum(arrange[i:i+7]) == 7):
        answer = "YES"
        break
print(answer)







