
#  -1 crime occured 






n = int(input())
data =  list(map(int , input().split()))
counter = 0
officer = 0
for i in data:
    if(i != -1):
        officer += i
    elif(officer == 0 and i == -1):
        counter +=1
    else:
        officer -= 1
print(counter)