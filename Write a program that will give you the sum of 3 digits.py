num=int(input("Enter three digit number: "))

a=num%10
num=num//10
b=num%10
c=num//10
sum=a+b+c
print(sum)
