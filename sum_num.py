# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     if(i%2==0):
#         sum=sum+i
# print(sum)


# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     if(i%2!=0):
#         sum=sum+i
# print(sum)

n=int(input("Enter the number"))
sum=0
for i in range(0,n+1):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)