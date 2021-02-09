n = int(input())

X, Y, Z = map(int, input().split())
for i in range(n-1):
    x, y, z = map(int, input().split())
    X += x
    Y += y
    Z += z
if(X == 0 and Y == 0 and Z == 0 ):
    print('YES')
else:
    print('NO')
