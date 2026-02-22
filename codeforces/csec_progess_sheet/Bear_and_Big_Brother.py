# leamak weight triplle after every year 
# bob weight double 

# how many year to leamke be >


[lemak , bob] = map(int , input().split())
count = 0
while(True):
    bob =  bob * 2
    lemak =  lemak * 3 
    count += 1 
    if(lemak > bob):
        print(count)
        break

