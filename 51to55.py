#51. Check Palindrome Number
number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#52. Happy Number
number = int(input("Enter a number: "))

while number != 1 and number != 4:
    sum = 0

    while number > 0:
        digit = number % 10
        sum = sum + digit * digit
        number = number // 10

    number = sum

if number == 1:
    print("It is a Happy number")
else:
    print("It is not a Happy number")

#53. Product of Digits
number = int(input("Enter a number: "))

number = abs(number)
product = 1

if number == 0:
    product = 0
else:
    while number > 0:
        digit = number % 10
        product = product * digit
        number = number // 10

print("Product of digits =", product)

#54. Extract and Print Each Digit
number = int(input("Enter a number: "))

number = abs(number)

print("Digits are:")

while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10

#55. Factorial of N
n = int(input("Enter a number: "))

factorial = 1


for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial of", n, "=", factorial)

