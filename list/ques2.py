#  2.Copy the Array
#  You are given a constant array A and an integer B.
#  You are required to return another array where Arr[i] = A[i] + B.
#  Input :
# A=[1 2 3 2 1]
#  B=3
#  Output:
#  [4 5 6 5 4]

A = list(map(int, input("Enter numbers: ").split()))
B=3
C=[]
for i in A:
    C.append(i + B)
print(C)

