# Problem: Fox And Snake
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/510/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. accept 2 inputs number lines and  cols
# 2.loop with the number of lines
# 3. if l is even print cols * #
# 4. here use other if else with one variable true and f to make # to foront and end if odd print . * cols-1 , #



[lines , cols] = list(map(int , input().split(" ")))
end = True
for i in range(lines):
    if i % 2 == 0 :
        print("#" * cols)
    else:
        if end:
            print("." *(cols-1)+"#")
            end = not end
        else:
            print("#"+"." *(cols-1))
            end = not end

