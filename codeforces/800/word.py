# Problem:  Word
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/59/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept inputs which is the word contain both upper and lower
# 2. filter the letter and create 2 section UPPer_letter and lower letter 
# 3. then if lower >= upper word.upper else word.lower
# -------------------------------


mix_word =  list(input().strip())
lower_words =  list(filter (lambda x : x.lower() == x , mix_word))
upper_words =  list(filter (lambda x : x.upper() == x , mix_word)) 
join_word =  "".join(mix_word)
if(len(lower_words) >= len(upper_words)):
    print(join_word.lower())
else:
    print(join_word.upper())    