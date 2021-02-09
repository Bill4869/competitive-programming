n, t = map(int, input().split())

s = list(input())

for i in range(t):
    j = 0
    while j < n - 1:
        if(s[j] == 'B' and s[j+1] == 'G'):
            dum = s[j]
            s[j] = s[j+1]
            s[j+1] = dum
            j += 2
        else:
            j += 1

print("".join(s))