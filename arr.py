# # given an array elements at every step remove element is equal to sum of array element present in the array find the minimum cost to remove all the elements.
# arr = [4, 2, 1]
# arr.sort()
# total=sum(arr)
# cost=0
# for x in arr:
#     cost = cost + total
#     total = total - x
# print(cost)

# # we have to delete  element and decreasing order in the cost

# arr = [4, 2, 1]
# arr.sort(reverse=True)
# total=sum(arr)
# cost=0
# for x in arr:
#     cost += total
#     total -= x
# print(cost)


# Given an array element to calculate number integers present to a[i] is said to no if number of elements < a[i]==a[i].
# arr=[1,-5,3,5,-10,4]
# # [-10,-5,1,3,4,5,10]
# for x in arr:
#     if arr.count(x)-1 == x:
#         print(x)

# given an int array k of size n return 1 if array can be arrange to form an ap otherwise return 0 if the difference b/w element is the same.
# arr=[1,2,3,4]
# arr.sort()
# b=arr[1]-arr[0]
# c=1
# for i in range(2,len(arr)):
#     if arr[i]-arr[i-1]!=b:
#         c=0
# print(c)

2 8 14 29 31 49 65 79 88 97
total runs code  last over
total runs code  code
total runs code  6 to 10

