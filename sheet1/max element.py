A = float(input("Enter first number (A): "))
B = float(input("Enter second number (B): "))
C = float(input("Enter second number (C): "))


if(A>B) and (A>C):
    print("Minimum:", A)
elif(B>A) and (B>C):
    print("minimum:", B)
else:
    print("Maximum",C)