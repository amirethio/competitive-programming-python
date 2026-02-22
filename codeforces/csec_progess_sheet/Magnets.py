



n =  int(input())
counter = 1
previous = ""
for i in range(n):
    if(i == 0):
        previous = input()
        continue
    magnet =  input()
    if(previous != magnet):
        counter +=1
        previous = magnet
print(counter)

        
        