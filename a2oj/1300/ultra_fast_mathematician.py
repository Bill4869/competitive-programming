n1 = input()
n2 = input()

n = ""
for i, j in zip(n1, n2):
    if(i != j):
        n += '1'
    else:
        n += '0'

print(n)