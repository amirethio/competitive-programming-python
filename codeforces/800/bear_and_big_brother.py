# Problem: Bear and Big Brother
# Difficulty: 800
# Link:https://codeforces.com/problemset/problem/791/A
# Status: Solved 


# -------------------------------
# Approach:
# 1. limak wants become larger than his brpther
# 2. accept a and b (limak_weight , brother's weight)
# 3. use while and by cheking each year until limak_weight > brother's weight
# 4. print tee result
# ------------------------------


limak_weight,bob_weight  = map(int ,input().split())
min_year = 0
while(True):
    limak_weight*= 3
    bob_weight*= 2
    min_year += 1
    if(limak_weight > bob_weight):
        print(min_year)
        break

