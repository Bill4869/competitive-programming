n = int(input())

if(n == 1 or n % 2 != 0):
    print(-1)
else:
    lis = [*range(1, n+1)]
    for i in range(0, n, 2):
        if(i+1 < n):
            dumm = lis[i]
            lis[i] = lis[i+1]
            lis[i+1] = dumm
    print(" ".join([str(i) for i in lis]))

