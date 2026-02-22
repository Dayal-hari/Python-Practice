## given an array A of N non negative numbers and a non negative number B, you need to find the number of subarrays in A with a sum less then B .
## we may assume that there id no overflow 


def solve(self, A, B):
    N = len(A)
    count = 0
    
    for i in range(N):
        sum1 = 0
        for j in range(i, N):
            sum1 += A[j]
            if sum1 < B:
                count += 1
            else:
                break
    return count


