k = int(input())

dic = {}
for i in range(4):
    a = input()
    for b in a:
        if (b.isnumeric()):
            if(b in dic):
                dic[b] += 1
            else:
                dic[b] = 1

for i in dic:
    if(dic[i] > k * 2):
        print('NO')
        break
else:
    print('YES')
