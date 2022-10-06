num1=int(input("Enter four degit number: "))
num=num1
a=num%10
num=num//10

b=num%10
num=num//10

c=num%10

d=num//10

reverse=1000*a+100*b+10*c+d
print(reverse)

print(f"Original Number is : {num1}")
print(f"reverse Number is : {reverse}")

if num==reverse:
    print(True)
else:
    print(False)

