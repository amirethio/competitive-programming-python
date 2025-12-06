# Problem:  Wrong Subtraction
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/977/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept inputs number given_number and substract_times
# 2.  loop  in  substract_times  and 
# 3. IF last didgit != 0 =>  -1
# 4. else : last didgit == 0 =>  /10
# 5. print out the final number aftera all substraction
# -------------------------------


given_number , substract_times =  map(int , input().strip().split())

for i in range(substract_times):
    if(str(given_number)[-1] !=  "0"):
        given_number -= 1
    else:
        given_number = int(given_number/ 10)
print(given_number)



    
# NOTE : instead if(str(given_number)[-1] !=  "0"): use given_number % 10 != 0