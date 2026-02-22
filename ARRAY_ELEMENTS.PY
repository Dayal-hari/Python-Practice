def arr(a):
    result=0
    for i in a:
        result=result^i
    return result
a=[1,2,3,4,3,2,4]
print(arr(a))