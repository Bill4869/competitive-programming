h, w = map(int, input().split())

s = []

for i in range(h):
    s.append(input())
ans = 0
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        for di in range(2):
            for dj in range(2):
                if(s[i+di][j+dj] == '#'):
                    cnt += 1
        
        if(cnt == 1 or cnt == 3):
            ans += 1

print(ans)