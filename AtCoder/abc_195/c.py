n = int(input())
ans = 0

dummy = 6
if(n < 1000):
    print(0)
else:
    while True:
        if(int('9' * dummy) >= n):
            ans += (n - (int('9' * (dummy - 3)))) * ((dummy - 1) // 3)
            break
        else:
            ans += (int('9' * dummy) - (int('9' * (dummy - 3)))) * ((dummy - 1) // 3)
            dummy += 3
    print(ans) 

