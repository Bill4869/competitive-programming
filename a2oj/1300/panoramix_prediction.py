def isPrime(n) : 
 
    # Corner cases 
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

n, m = map(int, input().split())
n += 1
while(not isPrime(n) and n <= m):
    n += 1
if(n == m):
    print("YES")
else:
    print("NO")
