# less than move and dce by one move 
# check until the last one is smaller 
# after 1 move vheck from 0




c = int(input())
arr = list(map(int , input().split()))
arr.sort()
result = ""
for i in arr:
    result =  result + f'{str(i)} '
print(result)











