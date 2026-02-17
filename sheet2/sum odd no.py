num = int(input("enter a number : "))
odd = 0
for i in range(1,num+1):
    if(i%2!=0):
        odd = odd + i
print(odd)        