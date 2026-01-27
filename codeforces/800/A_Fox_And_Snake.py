# Problem:  Fox And Snake
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/510/A
# Status: Solved 


# -------------------------------
# Approach:
# 1.accpt sets in baracket and change to set pitnt len of set
# 2.accpt sets in baracket and change to set pitnt len of set
# 3.accpt sets in baracket and change to set pitnt len of set
# 4.accpt sets in baracket and change to set pitnt len of set
# -------------------------------


input_sets = input()[1:-1].split()
input_sets = set("".join(input_sets).split(","))
if(input_sets == {''}):
    print(0)
else:
    print(len(input_sets))


# NOTE : you can split using " ,"





