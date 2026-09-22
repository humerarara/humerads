#1. Arithmetic Operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b

print("Sum =", sum)
print("Difference =", difference)
print("Product =", product)
print("Quotient =", quotient)
print("Remainder =", remainder)

# 2.Area of a Circle
radius = float(input("Enter radius: "))

pi = 3.14
area = pi * radius * radius

print("Radius =", radius)
print("Area of circle =", area)

# 3. Simple Interest 
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))

interest = (principal * rate * time) / 100

print("Principal =", principal)
print("Rate =", rate)
print("Time =", time)
print("Simple Interest =", interest)

#4.Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Celsius =", celsius)
print("Temperature in Fahrenheit =", fahrenheit)

#5. Divisibility by 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif number % 3 == 0:
    print("The number is divisible by 3 only")
elif number % 5 == 0:
    print("The number is divisible by 5 only")
else:
    print("The number is not divisible by 3 or 5")

#6.Relational and Logical Operators
 #Greater of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    greater = a
else:
    greater = b

print("Greater number =", greater)

#7.Positive, Negative or Zero
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#8.Check Three Numbers Equal
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All three numbers are equal")
else:
    print("All three numbers are not equal")

#9.Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#10. Uppercase, Lowercase, Digit or Special Character
ch = input("Enter a character: ")

if ch.isupper():
    print("The character is uppercase")
elif ch.islower():
    print("The character is lowercase")
elif ch.isdigit():
    print("The character is a digit")
else:
    print("The character is a special character")
