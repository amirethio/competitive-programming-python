# Problem: Chat room
# Difficulty: 1000
# Link: https://codeforces.com/problemset/problem/58/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept scrambled_word as int
# 2. filter and push to the new list
# 3. if its = hello => YES :  NO
# -------------------------------

# start from 1 and check if they can make hello in row
# first fins h and after h check if there is e l l o w
# if not find other h's 
# if there is not return NO





scrambled_word =  list(input().strip())
found =  False

for i in range(len(scrambled_word)):
    if(scrambled_word[i]== 'h'): 
        for j in range(i+1 ,len(scrambled_word)):
            if(scrambled_word[j] == 'e'):
                for k in range(j+1 ,len(scrambled_word)):
                    if(scrambled_word[k] == 'l'):
                        for l in range(k+1 ,len(scrambled_word)):
                            if(scrambled_word[l] == 'l'):
                                for m in range(l+1 ,len(scrambled_word)):
                                    if(scrambled_word[m] == 'o'):
                                        found = True

if(found):
    print("YES")
else:
    print("NO")

# ALTERNATIVE : use this way

scrambled_word =  input().strip()
count = 0 
found =  True
for i in scrambled_word:
    if(i == "hello"[count] ):
        count += 1
    if(count == 5):
        print("YES")
        break
if(count != 5):
    print("NO")


