def g1(n):
    return int(''.join(sorted(str(n))[::-1]))
def g2(n):
    return int(''.join(sorted(str(n))))
def f(n):
    return g1(n)-g2(n)
N,K = map(int,input().split())
for _ in range(K):
    N = f(N)
print(N)