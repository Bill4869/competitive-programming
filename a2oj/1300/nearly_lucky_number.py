n = [int(i) for i in input()]
luckyNum = [4, 7]
digit = n.count(4) + n.count(7)
if digit in luckyNum:
    print('YES')
else:
    print('NO')