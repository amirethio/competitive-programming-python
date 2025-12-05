# Problem: Helpful Maths
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/339/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accpt the string of sums of number 
# 2.split it using the + operator
# 3.then order the list  and print in order of increasing 
# -------------------------------




sum_string =  list(map(int , input().split("+")))
sum_string = sorted(sum_string)
final_string = ""
for i in range(len(sum_string)):
    if(i == 0 ):
        final_string = sum_string[i]
        continue
    final_string =  f'{final_string}+{sum_string[i]}'
print(final_string)


# NOTE : use .join to combine  "+".join(list_of_strings)

# eg 
# st =  "+".join(["1","2","3","4"])
# print(st)