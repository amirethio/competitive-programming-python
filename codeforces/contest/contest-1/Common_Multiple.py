# ?fonding max sixe of beacutyful subsequence 
# n no of test casw
# arr_len
# same value in array it crashes
# finding the common factor of all 
# set and count its length 



n = int(input())
for i in range(n):
    arr_len =  int(input())
    arr = list(map(int , input().split()))
    print(len(set(arr)))
