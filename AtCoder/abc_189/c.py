n = int(input())
a = list(map(int, input().split()))

ans = 0

for l in range(n):
    x = a[l]
    for r in range(l, n):
        x = min(x, a[r])
        ans = max(ans, x * (r + 1 - l))
print(ans) 
