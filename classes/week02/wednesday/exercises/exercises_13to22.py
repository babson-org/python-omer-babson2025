from classes.week00.second_class.utils import clear_screen

'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

pause = input('pause')
clear_screen()
'''
Enter a number: 2
Positive
'''

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

pause = input('pause')
clear_screen()


'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Both are positive")
elif a > 0 or b > 0:
    print("At least one is positive")
else:
    print("None are positive")

pause = input('pause')
clear_screen()


'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

pause = input('pause')
clear_screen()
'''
1
2
4
5
7
8
10
11
13
14
16
17
19
20
'''

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the secret number: "))
print("Correct!")

pause = input('pause')
clear_screen()
'''
Guess the secret number: 10
Guess the secret number: 8
Guess the secret number: 7
Correct!
'''

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
for i in range(1, 11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

pause = input('pause')
clear_screen()
'''
1
2
4
5
6
'''

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
def square(x):
    return x * x

print("Square of 5 is:", square(5))

pause = input('pause')
clear_screen()
'''
Square of 5 is: 25
'''

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
def add_item(lst, item):
    lst.append(item)

my_list = [1, 2, 3]
add_item(my_list, 4)
print("Updated list:", my_list)

pause = input('pause')
clear_screen()

'''
Updated list: [1, 2, 3, 4]
'''

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
def greet(name):
    # Print a greeting for the given name
    """
    This function takes a name as input
    and prints a friendly greeting.
    """
    print(f"Hello, {name}!")

greet("Omer")

pause = input('pause')
clear_screen()
'''
Hello, Omer!
'''

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
names = []
for i in range(5):
    n = input(f"Enter name {i+1}: ")
    names.append(n.capitalize())

names.sort()
print("Sorted names:", names)

pause = input('pause')
clear_screen()

'''
Enter name 1: Omer
Enter name 2: Sunny
Enter name 3: Abi
Enter name 4: Baba
Enter name 5: Anne
Sorted names: ['Abi', 'Anne', 'Baba', 'Omer', 'Sunny']
'''