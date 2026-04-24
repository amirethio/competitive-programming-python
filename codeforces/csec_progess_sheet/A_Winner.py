# end gate => max => winner




n =int(input())
db = {
}
inputs = []
for i in range(n):
    name , score = input().split()
    inputs.append(name +" " + score)
    if(name in db):
        db[name] += int(score)
    else:
        db[name] = int(score)
    values = list(db.values())
max = max(values)
if(values.count(max) > 1):
    equal = {}
    for i in inputs:
        name , score = i.split()
        if(name in equal):
            equal[name] += int(score)
        else:
            equal[name] = int(score)
        if(equal[name] >= max):
            print(name)
            break
else:
    items =  list(db.keys())
    index =  values.index(max)
    print(items[index])

