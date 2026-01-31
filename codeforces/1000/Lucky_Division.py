# Problem: Lucky Division
# Difficulty: 1000
# Link: https://codeforces.com/problemset/problem/122/A
# Status: Solved 


# -------------------------------
# Approach:
# -  luckey no =  +ve intiger with decimal digit 4 and 7 only
# 1. accept n the no to be checked
# 2.   check it the no contain only 4 and 7 using set 
# 3.   else check if its divisble by 4 or 7 else NO
# 4. almodt luckey => YES else => NO



# how can we find the all combination of luckey no less than 1000 which is the combination of 4 and 7
# check if it can be divided by a 


no = int(input())
no_ary = set(str(no))

for i in range(2 , no+2):

    if(i == no+1):
        print("NO")
        break
    if(no_ary <= {"7" , "4"}):
        print("YES")
        break
    elif(no%4 == 0 or no%7 == 0):
        print("YES")
        break
    if(no/i == int(no/i) and set(str(int(no/i))) <= {"7" , "4"}):
        print("YES")
        break

        
