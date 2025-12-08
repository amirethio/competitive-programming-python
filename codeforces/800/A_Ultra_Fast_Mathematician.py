# Problem:  Ultra-Fast Mathematician
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/61/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. aceept input and number_one and two and split them
# 2. same index differ = > 1 : => 0
# 3. loop over them and check if index vlaue same => prepend 0 : 1
# -------------------------------


number_one =  list(input().strip())
number_two =  list(input().strip())
final_answer = ""

for i in range(len(number_one)):
    if(number_one[i] == number_two[i]):
        final_answer += "0"
    else:
        final_answer += "1"
print(final_answer)