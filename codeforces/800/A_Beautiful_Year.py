# Problem: T Beautiful Year
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/271/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept the year which is given_year
# 2. increment 1 to that year until 
# 3. the new year is all distinct digit
# 4. check by nested loop  ot in operstor 
# -------------------------------


given_year = int(input())
new_year = given_year


while True:
    new_year += 1
    all_distinct = 0
    for i in range(4):
        split_year = str(new_year)
        if(split_year.count(split_year[i]) == 1):
            all_distinct+=1
    if(all_distinct == 4):
        break        
print(new_year)