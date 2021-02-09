n = int(input())
a = list(map(int, input().split()))

g = a.index(max(a))
a.reverse()
s = a.index(min(a))
# when move biggest from the other side the smallest is closer to the other side one step
if (g + s >= n):
    print(g + s - 1)
else:
    print(g + s)