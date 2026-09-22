#41. Clock Angle
hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour_angle = 30 * hour + 0.5 * minute
minute_angle = 6 * minute

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("Smaller angle =", angle)

#42. Scholarship Eligibility
marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 300000:
    print("Student is eligible for scholarship")
else:
    print("Student is not eligible for scholarship")

 #43. Print Numbers from 1 to N
 n = int(input("Enter the value of N: "))

print("Numbers from 1 to N:")

for i in range(1, n + 1):
    print(i, end=" ")

#44. Print Numbers from N to 1
n = int(input("Enter the value of N: "))

print("Numbers from N to 1:")

for i in range(n, 0, -1):
    print(i, end=" ")
#45. Print Even Numbers from 1 to N
n = int(input("Enter the value of N: "))

print("Even numbers:")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
#46. Print Odd Numbers from 1 to N
n = int(input("Enter the value of N: "))

print("Odd numbers:")

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
  #47. Sum of First N Natural Numbers
  n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of first", n, "natural numbers =", sum)
#48. Count Number of Digits
number = int(input("Enter a number: "))

number = abs(number)
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count = count + 1

print("Number of digits =", count)
#49. Sum of Digits
number = int(input("Enter a number: "))

number = abs(number)
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print("Sum of digits =", sum)
#50. Reverse a Number
number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number =", reverse)
