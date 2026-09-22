#25. Grade Calculation
marks = int(input("Enter marks: "))

if marks > 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade =", grade)

#26. Day of the Week
number = int(input("Enter a number from 1 to 7: "))

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Invalid number")

#27. Electricity Bill

units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Electricity Bill =", bill)

#28. Triangle Type
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#29. Valid Triangle
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("A valid triangle can be formed")
else:
    print("A valid triangle cannot be formed")

#30. Simple Calculator Using Switch-Case Equivalent
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b
else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result =", result)

#31. Number of Days in a Month
month = int(input("Enter month number: "))

if month == 2:
    days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif 1 <= month <= 12:
    days = 31
else:
    days = 0

if days == 0:
    print("Invalid month")
else:
    print("Number of days =", days)

#32. Positive/Negative and Even/Odd
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")

    if number % 2 == 0:
        print("It is even")
    else:
        print("It is odd")

elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#33. Three Numbers in Ascending Order
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    first = a
    second = b if b <= c else c
    third = c if b <= c else b
elif b <= a and b <= c:
    first = b
    second = a if a <= c else c
    third = c if a <= c else a
else:
    first = c
    second = a if a <= b else b
    third = b if a <= b else a

print("Ascending order:", first, second, third)


#34. Roots of Quadratic Equation
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b * b - 4 * a * c

if discriminant > 0:
    print("The equation has real and distinct roots")
elif discriminant == 0:
    print("The equation has real and equal roots")
else:
    print("The equation has imaginary roots")

#35. Alphabet, Digit or Special Character
character = input("Enter a character: ")

if character.isalpha():
    print("It is an alphabet")
elif character.isdigit():
    print("It is a digit")
else:
    print("It is a special character")

#36. Profit, Loss or No Profit/Loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No profit and no loss")

#37. Find the Quadrant
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point lies in Quadrant I")
elif x < 0 and y > 0:
    print("Point lies in Quadrant II")
elif x < 0 and y < 0:
    print("Point lies in Quadrant III")
elif x > 0 and y < 0:
    print("Point lies in Quadrant IV")
else:
    print("Point lies on an axis")

#38. Armstrong Number
number = int(input("Enter a three-digit number: "))

original = number
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit ** 3
    number = number // 10

if sum == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

#39. Salary with Overtime
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    salary = hours * rate
else:
    normal_salary = 40 * rate
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * rate * 1.5
    salary = normal_salary + overtime_salary

print("Total salary =", salary)

#40. ATM Withdrawal
amount = float(input("Enter withdrawal amount: "))
balance = float(input("Enter account balance: "))
minimum = float(input("Enter minimum balance: "))

available = balance - minimum

if amount <= available:
    print("Withdrawal approved")
    print("Remaining balance =", balance - amount)
else:
    print("Withdrawal rejected")
    print("Insufficient balance")
  
