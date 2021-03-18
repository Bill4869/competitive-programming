n = int(input())

a = list(map(int, input().split()))

left = max(a[0:len(a)//2])
right = max(a[len(a)//2:len(a)])

second = min(left, right)

ans = a.index(second) + 1

print(ans)