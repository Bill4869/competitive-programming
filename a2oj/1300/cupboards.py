n = int(input())
left = []
rith =[]
for i in range(n):
    l, r = map(int, input().split())
    left.append(l)
    rith.append(r)

ans = min(left.count(1), left.count(0)) + min(rith.count(1), rith.count(0))
print(ans)
