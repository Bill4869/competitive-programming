row = 0
collumn = 0
for i in range(5):
    nums = list(map(int, input().split()))
    if (1 in nums):
        row = i
        collumn = nums.index(1)
        break

moves = abs(row - 2) + abs(collumn - 2)
print(moves)