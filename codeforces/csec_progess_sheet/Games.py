# n·(n - 1) games 
# check only where home and guest are the same 

n = int(input())
home = []
away = []
count = 0 
for i in range(n):
    a , b = input().split()
    home.append(a)
    away.append(b)
for i in range(n):
    if(home[i] in away):
        count += away.count(home[i])
print(count)