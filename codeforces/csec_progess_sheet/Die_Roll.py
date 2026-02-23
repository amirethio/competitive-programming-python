#  Yakko pannn
# Wakko tanmi 
# Dot transi



maximum = 7 - max(map(int , input().split()))
denominator = 6

if(maximum % 3 == 0):
    maximum = maximum / 3
    denominator = denominator/3
if(maximum % 2 == 0):
    maximum = maximum/2
    denominator = denominator/2

print(f'{int(maximum)}/{int(denominator)}')

