# Problem: Kefa and First Steps
# Difficulty: 900
# Link:https://codeforces.com/problemset/problem/580/A
# Status: Solved 


# -------------------------------
# Approach:
# - finding maximum no decreasing subsequent
# 1. accept days and accept the sequence of numbers = mooney
# 2. declare a vaiable to store the max_suequence  and a pointer 
# 3. start from the first one and loop  and increment by 1 the max.. until it decrease and make the pinter min valur
# 4.when it decrease loop again starting from the the pointer



days = int(input())
money = list(map(int , input().split()))

max_sequence_no = 1
max_sequence_ary = []
index = 0

while(index < len(money)):
    if( index < len(money)-1 and money[index] <= money[index+1]):
        max_sequence_no += 1
    else:
        max_sequence_ary.append(max_sequence_no)
        max_sequence_no =  1
    index +=1
if(max_sequence_ary == []):
    print(len(money))
else:
    print(max(max_sequence_ary))



