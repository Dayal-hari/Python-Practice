# n=int(input("enter the number"))
# for i in range(1,n+1):
#         print("*",end=" ")
#         for j in range(1,n+1-i):
#             print("_",end=" ")
# print()

n=int(input("enter the number"))
for i in range(1,n+1):
        print(" ",end=" ")
        for j in range(i):
            print("_",end=" ")
        for j in range(i):
            print("*",end=" ")
        print( )