n, x = map(int, input().split())
 
li = list(map(int,input().split()))
li2 = (list(filter((x).__ne__, li)))
li2 = [str(i) for i in li2]
print(" ".join(li2))