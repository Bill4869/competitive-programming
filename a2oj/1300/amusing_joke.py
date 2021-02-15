guest = list(input())
host = list(input())
pile = list(input())

gh = guest + host
gh.sort()
pile.sort()

if(gh == pile):
    print("YES")
else:
    print("NO")

