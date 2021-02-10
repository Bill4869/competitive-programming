s = input()
lc = 0
uc = 0
for i in s:
    if(ord(i) >= 97):
        lc += 1
    else:
        uc += 1
    if(lc > (len(s) // 2) or uc > (len(s) // 2)):
        break

if(uc > lc ):
    print(s.upper())
else:
    print(s.lower())