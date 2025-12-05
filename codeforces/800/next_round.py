# Problem: Next Round
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/158/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. n = no of particpants  , k = the minimum  pass rank
# 2. accept paticipant and min pass rank
# 3. arrange the array in incrising order sort 
# find the pass mark which the kth  place participant // if at least one is +ve
# 4. filter from the array the one which get = or more than pass mark
# -------------------------------



[n, k] = input().split()
score = input().split()
score  = list(map(int , score))
minimum_rank =  score[int(k)-1]
if(score[0] == 0):
    passed_number = 0
else:
    passed_number =  len(list(filter(lambda x : x >= minimum_rank and x != 0 , score)))
print(passed_number)



