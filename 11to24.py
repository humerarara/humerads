#Bitwise Operators
#11. Even or Odd Using Bitwise AND
number = int(input("Enter a number: "))

result = number & 1

if result == 0:
    print("The number is even")
else:
    print("The number is odd")

#12.Swap Two Numbers Using XOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)

#13. Left Shift and Right Shift
number = int(input("Enter a number: "))

left = number << 1
right = number >> 1

print("Original number =", number)
print("After left shift =", left)
print("After right shift =", right)

#14. Check Kth Bit
number = int(input("Enter a number: "))
k = int(input("Enter the bit position: "))

value = number & (1 << k)

if value != 0:
    print("The kth bit is set")
else:
    print("The kth bit is not set")

#15. Count Number of Set Bits
number = int(input("Enter a number: "))

binary = bin(number)
count = binary.count("1")

print("Binary representation =", binary)
print("Number of set bits =", count)

Conditional Statements
#16. Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#17. Leap Year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

#18. Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
elif b > a:
    print("Largest number =", b)
else:
    print("Both numbers are equal")

#19. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)

#20. Vowel or Consonant
ch = input("Enter an alphabet: ")
ch = ch.lower()

if ch in "aeiou":
    print("The character is a vowel")
else:
    print("The character is a consonant")

#21. Ticket Pricing
age = int(input("Enter customer's age: "))

if age < 12:
    price = 50
elif age < 60:
    price = 100
else:
    price = 70

print("Ticket price =", price)

#22. Age Category
age = int(input("Enter age: "))

if age < 13:
    print("Category: Child")
elif age < 20:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")

#23. Time Greeting
hour = int(input("Enter hour: "))

if hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
elif hour < 21:
    print("Good Evening")
else:
    print("Good Night")

#24. Login Validator
username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")

