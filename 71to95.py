PYTHON PRACTICE PROGRAMS 71–95
=================================

PROGRAM 71
----------
# Convert decimal to binary
n = int(input("Enter decimal number: "))
binary = ""

if n == 0:
    binary = "0"

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary =", binary)


PROGRAM 72
----------
# Convert binary to decimal
b = input("Enter binary number: ")
decimal = 0

for digit in b:
    decimal = decimal * 2 + int(digit)

print("Decimal =", decimal)


PROGRAM 73
----------
# Read numbers until -1, print count and average
count = 0
total = 0

while True:
    n = int(input("Enter number: "))

    if n == -1:
        break

    total += n
    count += 1

print("Count =", count)

if count > 0:
    print("Average =", total / count)


PROGRAM 74
----------
# Sum of series: x^3/3! + x^5/5! + x^7/7! + ...
import math

x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))
s = 0

for i in range(n):
    p = 2 * i + 3
    s += x ** p / math.factorial(p)

print("Sum =", s)


PROGRAM 75
----------
# Palindrome check using recursion
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

s = input("Enter a string: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


PROGRAM 76
----------
# Count vowels in a string
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)


PROGRAM 77
----------
# Increasing + Decreasing using recursion
def print_num(n):
    if n == 0:
        return

    print_num(n - 1)
    print(n, end=" ")

n = int(input("Enter N: "))
print_num(n)

for i in range(n, 0, -1):
    print(i, end=" ")


PROGRAM 78
----------
# Right-angled triangle
n = 4

for i in range(1, n + 1):
    print("*" * i)


PROGRAM 79
----------
# Inverted right-angled triangle
n = 4

for i in range(n, 0, -1):
    print("*" * i)


PROGRAM 80
----------
# Right-aligned triangle
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


PROGRAM 81
----------
# Inverted right-aligned triangle
n = 4

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)


PROGRAM 82
----------
# Pyramid (centered)
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


PROGRAM 83
----------
# Inverted pyramid
n = 4

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


PROGRAM 84
----------
# Diamond shape
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


PROGRAM 85
----------
# Hollow rectangle
r = 4
c = 6

for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


PROGRAM 86
----------
# Hollow right-angled triangle
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


PROGRAM 87
----------
# Sandglass / Hourglass
n = 4

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


PROGRAM 88
----------
# Number triangle (row-wise)
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


PROGRAM 89
----------
# Sequential number triangle
n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


PROGRAM 90
----------
# Floyd's triangle
n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


PROGRAM 91
----------
# 1-0 alternating triangle
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()


PROGRAM 92
----------
# Pascal's triangle
n = 5

for i in range(n):
    value = 1
    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)

    print()


PROGRAM 93
----------
# Number pyramid (centered)
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        print(j, end=" ")

    print()


PROGRAM 94
----------
# Inverted number triangle
n = 4

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


PROGRAM 95
----------
# Column-wise incrementing
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
