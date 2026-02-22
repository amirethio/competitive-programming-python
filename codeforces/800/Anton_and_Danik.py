


n = int(input())
game = list(input())
count = 0
for i in game:
    if(i == 'A'):
        count = count + 1
    else:
        count = count-1 
if(count > 0):
    print("Anton")
elif(count < 0):
    print("Danik")
else:
    print("Friendship")