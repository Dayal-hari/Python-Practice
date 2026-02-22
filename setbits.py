# Given an in n,count howmany set bits are there in the integer
# n = int(input("Enter a number: "))
# count = 0

# while n > 0:
#     if n & 1:
#         count += 1
#     n = n >> 1

# print("Number of set bits:", count)


# given an array of n integers where all numbers occurs and even numbres of time access 1
# which occurs odd num 0
# input contain integer n denotting the size of array 
# next line n space seprated integers denotting the element contains

n=int(input("Enter the num :"))
a=list(map(int,input("Enter the element in array :").split()))
b=0
for i in a:
    b=b^i
print(i)