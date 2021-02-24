x = int(input())
ans = x
while(ans == x or ans % 100 != 0):
    ans += 1
print(ans - x)