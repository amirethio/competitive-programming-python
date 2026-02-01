# Problem:Cheap Travel
# Difficulty: 1200
# Link:https://codeforces.com/problemset/problem/466/A
# Status: Solved 


# -------------------------------
# Approach:
# - one ride subway ticket costs a rubles
# - special ticket (m) = amount = costs b rubles.
#  - find the mminimum  sum of money she will have to spend 
# 1. accept those inputs [rides_no , special_no,normal_price  , specail_prices]
# 2. first compair the one which is small special Vs normal
# 3. if noraml small multiply and print 
# 4. else count as the no of speciall if its can't be zero add normal using //


[rides_no, special_no, normal_price, special_price] = list(map(int, input().split()))

if normal_price <= (special_price / special_no):
    print(int(rides_no * normal_price))
elif rides_no % (special_no / special_price) == 0:
    print(int(rides_no * (special_price / special_no)))

else:
    special = int(rides_no / special_no)
    normal = rides_no - (special_no * special)
    special_noraml = (special * special_price) + (normal * normal_price)
    special_only = (special * special_price) + special_price
    if(special_noraml <= special_only):
        print(int(special_noraml))
    else:
        print(int(special_only)) 



# * instead of my code the best way of doing it is callculate the  possible ways then finally compair then print the result 



# rides_no, special_no, normal_price, special_price = map(int, input().split())

# cost_all_normal = rides_no * normal_price
# cost_all_special = ((rides_no + special_no - 1) // special_no) * special_price
# cost_mixed = (rides_no // special_no) * special_price + (rides_no % special_no) * normal_price

# print(min(cost_all_normal, cost_mixed, cost_all_special))

    
