# each sec black screen appear 
# ai calori fo every click 




no = list(map(int , input().split()))
calori = list(map(int , list(input())))
result = 0
for i in calori:
    result += no[i-1]
print(result)