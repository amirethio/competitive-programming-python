# find max k she garantee to win
# in new array push by finding the max of each or compair and push
# # for i in range(cases):






cases = int(input())
for i in range(cases):
    minimum = []
    len_arr = int(input())
    arr = list(map(int , input().split()))
    for i in range(len_arr):
        for j in range(i+2 ,len_arr+1):
            minimum.append(max(arr[i:j]))
    print(min(minimum)-1)

