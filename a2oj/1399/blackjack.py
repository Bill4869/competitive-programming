n = int(input())

if(n <= 10 or n > 21):
    print(0)
elif((n - 10 >= 1 and n - 10 <= 9) or n - 10 == 11):
    print(4)
else:
    print(15)
