#  3.Max and Min of an Array
#  Take input an array A of size N and write a program to print maximum and minimum
#  elements of the input array .Here N represents the length of the array .
#  Input :
# A=[1 2 3 4 5]
#  Output:
#  5 1

l=list(map(int,input("Enter the Elements :").split()))
a=max(l)
b=min(l)
print(a,b)

