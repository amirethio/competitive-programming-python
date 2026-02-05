# n houses k possible color 
# no adj house same color 
# 




houses , colors = map(int , input().split())
arr = list(map(int , input().split()))
max = 0
count = 1
for i in range(houses):
    if(i == houses-1 ):
        if(count >  max):
            max =  count
        break
    if(arr[i] != arr[i+1]):
        count = count + 1
    elif(count >  max):
        max =  count
        count = 1
    else:
        count = 1
print(max)