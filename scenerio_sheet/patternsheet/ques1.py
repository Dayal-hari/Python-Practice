# 1.
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n=int(input())
# m=int(input())
# for i in range(0,n):
#     for j in range(0,m):
#         print("*",end=" ")
#     print()

# 2. 
# *  
# * * 
# * * *  
# * * * *  
# * * * * *  

# n=int(input())
# for i in range(0,n):
#     for j in range(0,i+1):
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
#     for j in range(i):
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
# m=int(input())
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if(j==1 or j==n):
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
# for i in range(n,0,-1):
#     for j in range(i):
#         if(j==0 or j==i-1):
#             print("*",end=" ")
#         else:
#             print("-",end=" ")
#     print()  

# 7. 
#  _ _ _ _*        
#  _ _ _ * *           
#  _ _ *  * *           
#  _  * *  * * 
#   *  * *  * * 

# n=int(input())
# for i in range(1,n):
#     for j in range(n-i-1):
#         print("-",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# 8. 
 
# *   * * * *          
# _  * * * *        
# _ _ * * *         
# _ _ _*  *        
# _ _ _ _*  


# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print("-",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()

# 9. 
 
# ********** 
# ****  **** 
# ***    *** 
# **      ** 
# # *        * 

n = int(input())
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print("*", end="")
    for j in range(2 * (i - 1)):
        print(" ", end="")
    for j in range(n - i + 1):
        print("*", end="")
    print()

# 10. 
 
# *        * 
# **      ** 
# ***    *** 
# ****  **** 
# **********    
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(n - i + 1):
#         print("*", end="")
#     for j in range(2 * (i - 1)):
#         print(" ", end="")
#     for j in range(n - i + 1):
#         print("*", end="")
#     print()

# 11**********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********   
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(n - i + 1):
#         print("*", end="")
#     for j in range(2 * (i - 1)):
#         print(" ", end="")
#     for j in range(n - i + 1):
#         print("*", end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(n - i + 1):
#         print("*", end="")
#     for j in range(2 * (i - 1)):
#         print(" ", end="")
#     for j in range(n - i + 1):
#         print("*", end="")
#     print()

    
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
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

# 14. 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 


# n=int(input())
# m=1
# for i in range(1,n):
#     for j in range(i):
#         print(m,end=" ")
#         m+=1
#     print()


# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# * * 
# * * * 
# * * * * 

# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
    
# * * * * * 
# * * 
# * * 
# * * 
# * * * * * 
# n=int(input())
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*"*2)
#     print()
    

# n = 5 
# * * 
# * * 
# * 
# * * 
# * * 

# n=int(input())
# for i in range(1,n+1):
#     if(i==3):
#         print("*")
#     else:
#         print("*"*2)
#     print()

# n=int(input())
# count=0
# for i in range():
#     b=n%10
#     count=count+1
#     n//=10
# print(count)
# n=int(input())
# sum=0
# for i in range(n):
#     b=n%10
#     sum=sum+b
#     n=n//10
# print(sum)

n=input()
if(n[:]==n[::-1]):
    print("Yes")
else:
    print("No")

