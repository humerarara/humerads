PYTHON PRACTICE PROGRAMS 56–70
=================================

PROGRAM 56
----------
# Check whether a number is prime
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


PROGRAM 57
----------
# Print all prime numbers from 1 to N
n = int(input("Enter N: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")


PROGRAM 58
----------
# GCD / HCF of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)


PROGRAM 59
----------
# LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("LCM =", lcm)


PROGRAM 60
----------
# Fibonacci series up to N terms
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


PROGRAM 61
----------
# Sum: 1 + 1/2 + 1/3 + ... + 1/N
n = int(input("Enter N: "))
s = 0

for i in range(1, n + 1):
    s += 1 / i

print("Sum =", s)


PROGRAM 62
----------
# Sum: 1 - 2 + 3 - 4 + ... +/- N
n = int(input("Enter N: "))
s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        s -= i
    else:
        s += i

print("Sum =", s)


PROGRAM 63
----------
# Find x^n without pow()
x = int(input("Enter x: "))
n = int(input("Enter n: "))
result = 1

for i in range(n):
    result *= x

print("Answer =", result)


PROGRAM 64
----------
# Compute 1! + 2! + 3! + ... + N!
n = int(input("Enter N: "))
fact = 1
s = 0

for i in range(1, n + 1):
    fact *= i
    s += fact

print("Sum =", s)


PROGRAM 65
----------
# Multiplication table
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


PROGRAM 66
----------
# Sum of even and odd numbers from 1 to N
n = int(input("Enter N: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Even sum =", even)
print("Odd sum =", odd)


PROGRAM 67
----------
# Check if a number is an Armstrong number
n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
s = 0

while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")


PROGRAM 68
----------
# Find the largest and smallest digit
n = int(input("Enter a number: "))
digits = str(n)

largest = int(digits[0])
smallest = int(digits[0])

for ch in digits:
    d = int(ch)
    largest = max(largest, d)
    smallest = min(smallest, d)

print("Largest =", largest)
print("Smallest =", smallest)


PROGRAM 69
----------
# Print all factors of a number
n = int(input("Enter a number: "))

print("Factors:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


PROGRAM 70
----------
# Check whether a number is a perfect number
n = int(input("Enter a number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
