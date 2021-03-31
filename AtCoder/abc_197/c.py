n = input()

a = list(map(int, input().split()))

def bitwiseOr(lis):
    ans = lis[0]
    for i in range(1, len(lis)):
        ans = ans | lis[i]
    return ans

ans = -1
for i in range(len(a)-1):
    l = a[:i+1]
    r = a[i+1:]

    or_l = bitwiseOr(l)
    or_r = bitwiseOr(r)

    if(ans == -1):
        ans = or_l ^ or_r
    else:
        ans = min(ans, or_l ^ or_r)

print(ans)



