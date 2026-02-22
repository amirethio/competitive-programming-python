# current time 
# time slept 


current = list(map(int , input().split(":")))
slept = list(map(int , input().split(":")))
current_min = (current[0]*60) + current[1]
slept_min = (slept[0]*60) + slept[1]
final_min = current_min - slept_min

if(final_min < 0 ):
    final_min = 24*60 + final_min
    hour = final_min // 60 
    minutes = final_min % 60

else:
    hour = final_min // 60 
    minutes = final_min % 60
final = [str(hour) , str(minutes)]

if(len(final[0]) == 1):
    final[0] = f'0{final[0]}'
if(len(final[1]) == 1):
    final[1] = f'0{final[1]}'
print(f'{final[0]}:{final[1]}')