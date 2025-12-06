# Problem: Nearly Lucky Number
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/110/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept inputs number given_number 
# 2.luckey number =  number which are 4 and 7 
# 3. find the number of luckey_digits  =  loop and incremnt
# 4. if luckey_digits includes in a luckey no then => YES
# 5. else = > NO
# -------------------------------


number_given  = list(input().strip())
number_given =list( map(int ,number_given ))
luckey_digits = 0 
partial_luck  = 1
for i in number_given :
    if(i == 7 or i == 4):
        luckey_digits += 1
    else:
        partial_luck = 0
if(luckey_digits in number_given and luckey_digits != 0):
    print("YES")
else:
    print("NO")