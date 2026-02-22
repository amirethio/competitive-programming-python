# given h hours and h minute  24 format
# find miute before new year 



n = int(input())
day = 24*60
for i in range(n):
    [hour , minute] = map(int , input().split())
    print(day-((hour*60 )+(minute)))

    