# Problem:  Beautiful Matrix
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/281/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept the word
# 2. use capitalize ot chnage index 0 of word 
# 3. print tee result
# -------------------------------

random_word  = list(input().strip())
random_word[0] =  random_word[0].capitalize()
output_str =  "".join(random_word)
print(output_str)
