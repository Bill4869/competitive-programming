n = int(input())
t = list(input().split())
 
a = {}
 
for i in t:
    num = int(i) + 200
    if num in a:
        a[num] += 1
    else:
        a[num] = 1
 
key = list(a.keys()) 
res = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        dif = key[i] - key[j]
        res += a[key[i]] * a[key[j]] * (dif * dif)
 
print(res)