PYTHON PRACTICE PROGRAMS 96–112
=================================

PROGRAM 96
----------
# Reverse number triangle
n = 4

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


PROGRAM 97
----------
# Binary number triangle
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print((i + j + 1) % 2, end=" ")
    print()


PROGRAM 98
----------
# Alphabet triangle (row repeat)
n = 4

for i in range(n):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end=" ")

    print()


PROGRAM 99
----------
# Alphabet triangle (sequential)
n = 4

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()


PROGRAM 100
-----------
# Reverse alphabet triangle
n = 4

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


PROGRAM 101
-----------
# Right-aligned alphabet triangle
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        print(chr(65 + j), end=" ")

    print()


PROGRAM 102
-----------
# Alphabet pyramid (centered)
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        print(chr(65 + j), end="")

    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()


PROGRAM 103
-----------
# Butterfly pattern
n = 4

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


PROGRAM 104
-----------
# Hollow diamond inside rectangle
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        elif abs(i - n // 2) + abs(j - n // 2) == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


PROGRAM 105
-----------
# Number diamond
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


PROGRAM 106
-----------
# Zigzag pattern
n = 4

for i in range(1, n + 1):
    for j in range(1, 8):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


PROGRAM 107
-----------
# Spiral number matrix (4 x 4)
n = 4
a = [[0] * n for i in range(n)]

top, bottom = 0, n - 1
left, right = 0, n - 1
num = 1

while top <= bottom:
    for j in range(left, right + 1):
        a[top][j] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        a[i][right] = num
        num += 1
    right -= 1

    for j in range(right, left - 1, -1):
        a[bottom][j] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        a[i][left] = num
        num += 1
    left += 1

for row in a:
    print(*row)


PROGRAM 108
-----------
# Right arrow pattern
n = 4

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)


PROGRAM 109
-----------
# X pattern
n = 7

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


PROGRAM 110
-----------
# Plus (+) pattern
n = 7
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


PROGRAM 111
-----------
# Heart shape pattern
n = 6

for i in range(3):
    print(" " * (2 - i), end="")
    print("*" * (2 * i + 1), end=" ")
    print("*" * (2 * i + 1))

for i in range(6, 0, -1):
    print(" " * (6 - i) + "*" * (2 * i - 1))


PROGRAM 112
-----------
# Square with diagonals marked
n = 7

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        elif i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
