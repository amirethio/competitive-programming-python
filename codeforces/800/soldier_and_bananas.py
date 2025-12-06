# Problem:  Soldier and Bananas
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/546/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. w = banana  ,  n =  dollar   k 2k 3k ... => price
# 2. loop in rnage of w times  and found the proce of relistic banana calculated price
# 3. if (calculated price >=  our dollar) =>  calculated price-dollar
# 4.  else => 0
# -------------------------------


estimated_price , dollar , banana_no = map(int , input().strip().split())
calculated_price = 0
for i in range(1 , banana_no+1):
    calculated_price += i * estimated_price
if(calculated_price > dollar):
    print(calculated_price-dollar)
else:
    print(0)
