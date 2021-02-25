v, t, s, d = map(int, input().split())
 
start = v * t
end = v * s
 
if (d >= start and d <= end):
    print("No")
else:
    print("Yes")