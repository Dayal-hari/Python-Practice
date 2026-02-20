T=int(input())
ls=[]
for i in range(T):
    S=input()
    rev=''.join(reversed(S))
    if(S==rev):
        ls.append(1)
    else:
        ls.append(0)
for i in range(T):
    print(ls[i])