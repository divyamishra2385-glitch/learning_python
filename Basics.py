from email import message


print("hello World")
print("*" * 10)
students_count = 1000 
rating = 4.99
is_published = True
course_name = "Python Programming"
print(len(course_name))
# Numbers
print (10+3)
print (10-3)
print (10*3)
print (10/3)
print (10%3)
print (10**3)
print (10//3) 
# ⚖️ Comparison Operators in Python
#Comparison operators are used to compare two values.
#The result of every comparison is a Boolean value:
# `True`
# `False`
#These operators are commonly used in conditions, if statements, loops, and decision making.
print(10 > 3)
print(10 >= 10)
print(5 < 10)
print(5 <= 5)
print(10 == 10)
print(10 == "10")
print(10 != 5)
print("bag" > "apple")
print(ord("b"))
print(ord("B"))
#conditional statements
temperature = 35
if temperature > 30:
    print("it's warm")
    print("drink water")
print("done")
temperature = 15
if temperature > 30:
    print("it's warm")
    print("drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("done")
#ternary operator
Age = 22
message = "eligable" if Age >= 18 else "not eligable"
print(message)
#logical operator
high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

    high_income = False
good_credit = True
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not eligible")
#practice
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
#for loop
for number in range(3):
    print("Attempt", number + 1 ,(number + 1)*".")
for number in range(1,10,2):
    print("Attempt", number  ,(number )*".")
#for else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
#nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#iterable
for x in "python":
    print(x)
#whiole loop
#command = ""
#while command.lower() != "quit":
 #   command = input(">")
  #  print("ECHO", command)
#infinite loop

#while True:
 #   command = input(">")
  #  print("ECHO", command)
   # if command.lower() != "quit":
    #    break
    # Exercise

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
#Arguments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Divya", "Mishra")
#type of function
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

greet("Divya", "Mishra")
# Keyword Arguments (1:53:59)

def increment(number, by):
    return number + by

print(increment(2, by=1))
# Default Arguments
def increment(number, by=1):
    return number + by

print(increment(2))
print(increment(2, 5))
# Variable Number of Arguments (*args)
def multiply(*numbers):
    total = 1

    for number in numbers:
        total *= number

    return total

print(multiply(2, 3, 4, 5))
