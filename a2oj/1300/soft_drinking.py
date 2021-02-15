n, k, l, c, d, p, nl, np = map(int, input().split())

total_mil = k * l
total_lime = c * d
r = 0
while(total_mil - (n * nl) >= 0 and total_lime - n >= 0 and p - (n * np) >= 0):
    r += 1
    total_mil -= (n * nl)
    total_lime -= n
    p -= (n * np)

print(r)