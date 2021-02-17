import math

n = int(input())

even_num = 0
odd_num = 0
total_num = 0
even = ""
odd = ""
for i in range(n):
    if(i % 2 == 0):
        even += 'C'
        odd += '.'
        even_num += 1
    else:
        even += '.'
        odd += 'C'
        odd_num += 1
if (n < 3):
    print(n)
else:
    total_num += odd_num * (n // 2)
    total_num += even_num * math.ceil(n / 2)
    print(total_num)

for i in range(n):
    if(i % 2 == 0):
        print(even)
    else:
        print(odd)