# Problem: Anton and Letters
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/443/A
# Status: Solved 


# -------------------------------
# Approach:
# 1.accpt sets in baracket and change to set pitnt len of set
# -------------------------------

input_sets = input()[1:-1].split()
input_sets = set("".join(input_sets).split(","))
if(input_sets == {''}):
    print(0)
else:
    print(len(input_sets))


# NOTE : you can split using " ,"



