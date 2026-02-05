#  Berlandesk
#  user wants send name => no in db => ok
# else new name 
# new name = append - 1


n = int(input())
db = []
for i in range(n):
    name = input()
    if(name not in db):
        db.append(name)
        db.append(0)
        print("OK")
    else:
        index = db.index(name) + 1
        print(f'{name}{(db[index]+1)}')
        db[index] = db[index] + 1


