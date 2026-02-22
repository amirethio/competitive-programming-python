
# a < b : -1
# a > b : 1
# else 0






string_a = input().lower()
string_b = input().lower()
for i in range(len(string_a)):
    if(string_a < string_b):
        print(-1)
        break
    elif(string_a>string_b):
        print(1)
        break
    elif(i == len(string_a) -1):
        print(0)
