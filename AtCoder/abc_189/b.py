n, x = map(int, input().split())
x *= 100
ans = -1
current = 0
for i in range(n):
    v, p = map(int, input().split())
    current += p * v
    if(current > x):
        ans = i + 1
        break

print(ans)
