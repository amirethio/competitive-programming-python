# Problem: Queue at the School
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/266/B
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept children_number , transfer_time and stud_arrangement
# 2. loop transfer_time times and check andd when u find b => move it to the next index  , replace the place from previous 
# 3. print final arrnagement
# -------------------------------



children_number , transfer_time = map(int , input().split())
stud_arrangement = list(input())
for i in range(transfer_time):
    jump = False
    for i in range(children_number - 1):
        if(jump):
            jump = False
            continue
        if(stud_arrangement[i]=='B' and stud_arrangement[i+1]=='G'):
            stud_arrangement.pop(i)
            stud_arrangement.insert(i+1 , 'B')  
            jump = True

final_arrangement =  "".join(stud_arrangement)
print(final_arrangement)




# for i in range(transfer_time):
#     count = 0;
#     while (count != children_number-1):
#         if(stud_arrangement[count]=='B'):
#             print(count)
#             stud_arrangement.pop(count)
#             stud_arrangement.insert(count+1 , 'B')
#             print(stud_arrangement)
#             count +=2
#         else:
#             count +=1
# print(stud_arrangement)
    
        
