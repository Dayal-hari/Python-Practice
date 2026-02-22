#  1.Sum of list
#  Given an array compute the sum of all elements.
#  Input :
# A=[1 2345]
#  Output:
#  15

l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
    sum=sum+l[i]
print(sum)