




n  = int(input())
result = 0
for i in range(n):
    count = 0
    game =  list(map(int , input().split()))
    if(game.count(1) >= 2):
        result +=1
print(result)



