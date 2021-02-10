n = int(input())
t = input()

a = 0
for i in range(n - 1):
    if(t[i] == t[i+1]):
        a += 1
print(a)