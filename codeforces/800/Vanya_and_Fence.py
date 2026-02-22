# Vanya and Fence



# process 
# 1 should not exceed the height h 
# bend  width is 2 else 1 
# find the minimum width 

[n , fence_h] =  map(int , input().split())
person_height = list(map(int , input().split()))
width = 0

for i in person_height:
    q = i // fence_h 
    r = i % fence_h
    if(i <= fence_h):
        width = width + 1
    elif(q > 0 and r > 0):
        width = width + q + 1
    else:
        width = width + q
print(width)