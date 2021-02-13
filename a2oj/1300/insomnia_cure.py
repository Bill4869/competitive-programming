k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

ans = set()
ans.update([i for i in range(k, d + 1, k)])
ans.update([i for i in range(l, d + 1, l)])
ans.update([i for i in range(m, d + 1, m)])
ans.update([i for i in range(n, d + 1, n)])

print(len(ans))