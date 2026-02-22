






stri = input()
upper = 0
lower = 0
for i in stri:
    if(i == i.upper()):
        upper +=1
    else:
        lower +=1
if(upper >  lower):
    print(stri.upper())
else:
    print(stri.lower())