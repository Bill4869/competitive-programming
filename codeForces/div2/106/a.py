t = int(input())

for i in range(t):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())

    white = k1 + k2
    black = (2 * n) - white

    if(white // 2 >= w and black // 2 >= b):
        print('YES')
    else:
        print('NO')
