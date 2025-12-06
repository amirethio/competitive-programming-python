# Problem: Elephant
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/617/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. elephant can move 1, 2, 3, 4 or 5 positions  minumin_steps = ?
# 2. accept distance from user  then diving(//) by 5 then by the reminder of 1st 4 .... 
# 3. add the above quatient values
# -------------------------------


# distance = int(input().strip())
# elephant_steps = 0
# def onesteps(remind_distance):
#     global elephant_steps
#     return elephant_steps + remind_distance

# def two_steps(remind_distance):
#     global elephant_steps
#     elephant_steps += remind_distance//2
#     reminder =  remind_distance % 2
#     if(reminder > 0):
#        return onesteps(reminder)
#     else:
#         return elephant_steps 


# def theree_steps(remind_distance):
#     global elephant_steps
#     elephant_steps += remind_distance//3
#     reminder =  remind_distance % 3
#     if(reminder > 0):
#        return two_steps(reminder)
#     else:
#         return elephant_steps


# def foursteps(remind_distance):
#     global elephant_steps
#     elephant_steps += remind_distance//4
#     reminder =  remind_distance % 4
#     if(reminder > 0):
#        return theree_steps(reminder)
#     else:
#         return elephant_steps

# def fivestep(remind_distance):
#     global elephant_steps
#     elephant_steps += remind_distance//5
#     reminder =  remind_distance % 5
#     if(reminder > 0):
#        return foursteps(reminder)
#     else:
#         return elephant_steps



# final_step = fivestep(distance)
# print(final_step)


# NOTE : use short alternative way

# distance = int(input().strip())
# if(distance%5 == 0):
#     print(input // 5)
# else:
#     print((distance//5)+1)