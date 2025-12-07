# Problem: Calculating Function
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/486/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept number int
# 2. loop number times  from 1 to n+1
# 3. start with -  and next + and addup
# 4.Print result 
# -------------------------------


# an  =  int(input())
# if(an%2 == 0):
#     print(int(an/2))
# else:
#     print(int(-(an/2+1)))



#  NOTE: this doesn't work because of using float and we can't get a real specific value for big numbers 
# an  =  int(input())
# if(an%2 == 0):
#     n = ((an-2)/2) +1
#     m = n
#     even_sum = (n/2)*(2+an)
#     odd_sum = (m/2)*(-1-an+1)
# else:
#     m = abs(((-an+1)/-2)) + 1
#     n = abs(m-1)
#     odd_sum = (m)*((-1-an)/2)
#     even_sum = (n/2)*(2+an-1)
# print(int(even_sum+odd_sum))


