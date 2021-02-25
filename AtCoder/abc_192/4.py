x = input()
m = int(input())
 
def calBase(base, x, m):
    su = 0
    index = len(x) - 1
    for i in (x):
        su += i * pow(base, index)
        if(su > m):
            return False
        index -= 1
    return True

ans = 0
lis = [int(i) for i in x]

if(len(lis) == 1):
    if(lis[0] > m):
        print(0)
    else:
        print(1)
else:
    base = max(lis) + 1
    low = base
    high = m + 1
    ans = high
    while low <= high:
        index = (low + high) // 2
        output = calBase(index, lis, m)
        if(output):
            low = index + 1
        else:
            ans = min(index, ans)
            high = index - 1

    print(ans - base)