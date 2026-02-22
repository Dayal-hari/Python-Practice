mark1=int(input("Enter first number\n"))
mark2=int(input("Enter second number\n"))
mark3=int(input("Enter third number\n"))
mark4=int(input("Enter fourth number\n"))
mark5=int(input("Enter fifth number\n"))
per=(mark1+mark2+mark3+mark4+mark5)/500*100
if(per<100 or per>90):
    print("grade O:",per)
elif(per<90 or per>80):
    print("grade A:",per)
elif(per<90 or per>80):
    print("grade B:",per)
elif(per<80 or per>70):
    print("grade C:",per)
elif(per<70 or per>50):
    print("grade D:",per)
elif(per<0 or per>40):
    print("grade E:",per)
else:
    print("grade F:",per)
    