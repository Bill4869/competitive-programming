n = int(input())
 
for i in range(1, 1000001):
    if(int(str(i) * 2) > n):
        print(i - 1)
        break