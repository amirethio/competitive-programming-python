# Problem: Boy or Girl
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/236/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. odd no of character = male else=>female
# 2.accept the input which is a string 
# 3. remove duplicated letter 
# 4 .check its len if its odd =>IGNORE HIM! else "CHAT WITH HER!"  
# -------------------------------



user_name =  input().strip()
unique_string = ""
for i in user_name:
    if( not i in unique_string):
        unique_string =  unique_string + i
string_length =  len(unique_string)
if(string_length%2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")


# NOTE :  in here u can use set to  easily remove duplicated string characters
# eg: set(user_name) but set wornt preserve order
