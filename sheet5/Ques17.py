A=input()
A=A+A
vowel="aeiou"
res=""
for i in A:
    if i.isupper():
        continue
    else:
        if i in vowel:
            res+="#"
        else:
            res+=i
print(res)