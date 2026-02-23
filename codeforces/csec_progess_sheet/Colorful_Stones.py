 



standing = input()
colors = input()
counter = 1

for i in range(len(colors)):
    if(colors[i] == standing[counter-1]):
        counter += 1
    if(counter ==  len(standing)):
        break
print(counter)



