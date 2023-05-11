winners=set()
losers=set()
for i in range(int(input())):
    x, y = input().split()
    winners.add(x)
    losers.add(y)
print(sorted(winners-losers))