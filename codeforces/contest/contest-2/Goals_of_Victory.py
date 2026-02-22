# match once
# all score - get scored



n = int(input())
for i in range(n):
    teams_no = int(input())
    efficency = list(map(int , input().split()))
    print(0-sum(efficency))
    