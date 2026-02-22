# sanja = first 
# take left most or right most 










n = int(input())
cards_no =  list(map(int, input().split()))
Sereja = 0
Dima = 0 
start = 0
end = n-1
for i in range(n):
    if(i%2 == 0 or i == 0):
        if(cards_no[start] > cards_no[end]):
            Sereja += cards_no[start]
            start += 1
        else:
            Sereja += cards_no[end]
            end -= 1
    else:
        if(cards_no[start] > cards_no[end]):
            Dima += cards_no[start]
            start += 1
        else:
            Dima += cards_no[end]
            end -= 1

print(Sereja , Dima)