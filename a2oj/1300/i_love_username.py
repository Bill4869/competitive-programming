n = int(input())
scores = list(map(int, input().split()))

l = scores[0]
s = scores[0]
ans = 0
for i in range(1, len(scores)):
    if (scores[i] > l):
        ans += 1
        l = scores[i]
    elif (scores[i] < s):
        ans += 1
        s = scores[i]

print(ans)