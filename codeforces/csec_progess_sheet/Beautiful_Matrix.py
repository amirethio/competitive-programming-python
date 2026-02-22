#  beaufy if one is  at 3 x 3



# determine the place where 1 exist  in row and col
# find the substrucyionof abs and add
# 3-2 = 1
# abs(3 -5)  = -2


for i in range(5):
    row = list(map(int , input().split()))
    if(1 in row):
        row_no = i+1
        col_no =  row.index(1) +1
print(abs(3-row_no) + abs(3-col_no))