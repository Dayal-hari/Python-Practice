# n=int(input())
# m=int(input())
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# 3. 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=int(input())
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()



# 4. 
# 1  
# 1 *  
# 1 * 3  
# 1 * 3 *  
# 1 * 3 * 5  

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print("*",end=" ")
#         else:
#             print(j,end=" ")

#     print()


# 5. 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j==1) or (j==n):
#             print("*",end=" ")
#         else:
#             print("-",end=" ")
#     print()


# 6. 
# *_ _ _ _ _*
# *_ _ _ _*
# *_ _ _*
# *_ _*
# *_*


# n=int(input())
# for i in range(1,n+1):
#     print("*",end=" ")
#     for j in range(n-i):
#         print("-",end=" ")
#     if(i!=n):
#             print("*",end=" ")
#     print()

# _ _ _ _*
#  _ _ _ * *
#  _ _ *  * *
#  _  * *  * *
#   *  * *  * *

# n=int(input())
# for i in range(1,n+1):
#     print("-"* (n-i)+"*" * i )
# print()


# 12. 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 13. 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# n=int(input())
# for i in range(n,1,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()


# 14. 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

n=int(input())
num=0
for i in range(1,n+1):
    for j in range(1,i):
        print(num,end=" ")
        num=num+1
    print()