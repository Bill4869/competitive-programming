s = input()

index = 0
dictt = {'.': '0', '-.': '1', '--': '2'}
while index < len(s):
    if(s[index] in dictt):
        s = s.replace(s[index], dictt[s[index]], 1)
        index += 1
    else:
        s = s.replace(s[index:index+2], dictt[s[index:index+2]], 1)
        index += 1

print(s)
