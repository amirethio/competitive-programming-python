# min no for 2 neightbor dt color 





n = int(input())
color = input()
previous = color[0]
counter = 0
for i in range(1 ,n):
    if(previous == color[i]):
        counter +=1
    else:
        previous = color[i]
print(counter)

