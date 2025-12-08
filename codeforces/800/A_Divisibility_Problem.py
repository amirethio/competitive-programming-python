# Problem: Divisibility Problem
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/1328/A
# Status: Solved 


# -------------------------------
# Approach:
# 1.by move a = > a+1  
# 2. find min_move to make a//b == 0
# 3. accept test_case
# 4. loop thriugh test case and  and find min_div a//b 
# 5. answer is (min_div*b)+b
# -------------------------------

# for small value of n 
# test_case =   int(input())
# for i in range(test_case):
#     a , b = map(int , input().split())
#     count = 0
#     while True:
#         if((a+count)%b == 0):
#             print(count)
#             break
#         else:
#             count +=1



test_case =   int(input())
for i in range(test_case):
    a , b = map(int , input().split())
    if(a%b == 0):
        print(0)
        continue
    min_div =  (a // b)*b
    left = (min_div + b)-a
    print(left)



    