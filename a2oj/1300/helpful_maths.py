s = input()
s = [int(s[i]) for i in range(len(s)) if i % 2 == 0]
s.sort()
print('+'.join([str(i) for i in s]))