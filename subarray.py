# def ps(A,S,E):
#     for i in range(S,E+1):
#         print(A[i])
#     print()
# def printAllSub(A):
#     N=len(A)
#     for i in range(N):
#         for j in range(i,N):
#             ps(A,i,j)
# A=[1,2,3]
# printAllSub(A)

# the print of sum of every sub array

# def ps(A,S,E):
#     S=0
#     for i in range(S,E+1):
#         S=S+A[i]
#     print()
# def printAllSub(A):
#     N=len(A)
#     for i in range(N):
#         for j in range(i,N):
#             ps(A,i,j)
# A=[1,2,3]
# printAllSub(A)

# given an integer array nums find the subarray with largesst sum and returns its sum [-2,1,-3,4,-1,2,1,-5,4] output=6 [5,4,-1,7,8]

# def ps(A,S,E):
#     S=0
#     for i in range(S,E+1):
#         S=S+A[i]
#     print()
# def printAllSub(A):
#     N=len(A)
#     for i in range(N):
#         for j in range(i,N):
#             ps(A,i,j)
# A=[1,2,3]
# printAllSub(A)

# find the sum of all array sums
# find the sub array with the largest sum
# find the sum of subarray 
arr = [1, 2, 3, 4]
n = len(arr)

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr[j]
        print(f"Subarray {arr[i:j+1]} -> Sum = {current_sum}")
        

