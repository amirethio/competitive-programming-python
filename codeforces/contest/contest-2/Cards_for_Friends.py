# even will be cut in two two 
# enough yes else no
# finally mutiply by 2
#  
n = int(input())

for i in range(n):
    fold_1 =0 
    fold_2 = 0
    [wid ,  heig , friend] =  map(int , input().split())
    if(wid % 2 != 0 and heig%2 != 0):
        total = 1
    else:
        while(wid%2 == 0):
            fold_1 = fold_1 +1
            wid = wid/2
        while(heig%2 == 0):
            fold_2 = fold_2 +1
            heig = heig/2
        total = ((fold_1+fold_2)*2)+1
    if(total >= friend):
        print("YES")
    else:
        print("NO")


