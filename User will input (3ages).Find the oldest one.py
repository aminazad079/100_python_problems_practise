age1=int(input("Enter the first age: "))
age2=int(input("Enter the second age: "))
age3=int(input("Enter the third age: "))

max=age1
if max<age2:
    max=age2
elif max<age3:
    max=age3
print(f"The oldest age is {max}")