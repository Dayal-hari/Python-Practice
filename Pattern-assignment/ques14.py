n = int(input("enter a number :"))
B =1
for i in range(1,n+1):
    for j in range (1,i+1):
        print(B, end= " ")
        B+=1
    print()