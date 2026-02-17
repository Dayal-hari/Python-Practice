a=list(map(int,input().split()))
result=[]
for i in range(len(a)):
    if a[i]<0:
        result.append(a[i])
print(result)