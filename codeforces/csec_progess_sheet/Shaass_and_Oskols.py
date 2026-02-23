
wires = int(input())
birds_on_wire =  list(map(int , input().split()))
shot = int(input())
for i in range(shot):
    [wire_no , shot_bird] =  list(map(int , input().split()))
    up = (birds_on_wire[wire_no-1]-shot_bird);
    down = (shot_bird -1 )
    if(wire_no != (len(birds_on_wire))):
        birds_on_wire[wire_no] += up
    if(wire_no != 1):
        birds_on_wire[wire_no - 2] += down
    birds_on_wire[wire_no-1] = 0 

for i in birds_on_wire:
    print(i)

