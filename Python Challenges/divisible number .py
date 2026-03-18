# Write a program to check a number divisible by another number

num1 = int(input("Enter the Numerator: "))

num2 = int(input("Enter the Denomenator: "))

if num1 % num2 == 0:
    print(num1, "is divisible by", num2)

else:
    print(num1, "is not divisible by", num2)