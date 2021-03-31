h, w, x, y = map(int, input().split())
 
x -= 1
y -= 1
 
ans = 1
rows = []
 
for i in range(h):
    rows.append(input())
 
for i in range(x-1, -1, -1):
    if(rows[i][y] == '.'):
        ans += 1
    else:
        break
 
for i in range(x+1, h, 1):
    if(rows[i][y] == '.'):
        ans += 1
    else:
        break
 
for i in range(y-1, -1, -1):
    if(rows[x][i] == '.'):
        ans += 1
    else:
        break
 
for i in range(y+1, w, 1):
    if(rows[x][i] == '.'):
        ans += 1
    else:
        break
 
print(ans)