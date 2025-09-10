from classes.week00.second_class.utils import clear_screen
'''
# 1


Write down the steps a program would need to make a cup of tea. Then implement a Python
function make_tea() that prints each step.
'''
def make_tea():
    steps = [
        "Boil water",
        "Place the tea bag in the cup",
        "Pour the boiled water into the cup",
        "Remove the tea bag",
        "Drink"
    ]
    for step in steps:
        print(step)
make_tea()


pause=input('pause')
clear_screen()
'''
#2


Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
nums = [2, 4, 6, 8, 10]


def new_func(nums):
    return [nums[-1] + (i+1)*2 for i in range(3)]


print(new_func(nums))


pause=input('pause')
clear_screen()
'''
#3


Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
first = input(“What is your first name: ")
last = input(“What is your last name: ")


print(f"Hello,  {first} {last}")


pause=input('pause')
clear_screen()
'''
#4


Write a program that prints your Python version and platform using the sys and platform modules.
'''
import sys
import platform


print("Python version:", sys.version)
print("Platform:", platform.system(), platform.release())

#pprint.pprint(dir(sys))
print(type(sys.version))
print(sys.version, sys.platform)

pause=input('pause')
clear_screen()
'''
#5


Ask the user to input two numbers. Calculate and print their sum, difference, product,
and division (both / and //).
'''
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))


print(f"Sum: {x + y}")
print(f"Difference: {x - y}")
print(f"Product: {x * y}")
print(f"Division (/): {x / y}")
print(f"Floor Division (//): {x // y}")


pause=input('pause')
clear_screen()
'''
Enter the first number: 5
Enter the second number: 9
Sum: 14
Difference: -4
Product: 45
Division (/): 0.5555555555555556
Floor Division (//): 0
'''
#6


Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter
capitalized, and split it into words.
'''
sentence = input("Enter a sentence: ")


print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
print("Split into words:", sentence.split())


pause=input('pause')
clear_screen()
'''
#7


Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# Without parentheses
print(10 + 2 * 5 / 2 - 3 ** 2)   # 6.0


# With parentheses
print(((10 + 2) * 5) / 2 - (3 ** 2))   # 21.0

print(x)

x = 2**3**2
print(x)
pause=input('pause')
clear_screen()
'''
#8


Create a list of your three favorite foods. Replace the second item with a new one,
then print the list.
'''
# Create a list of three favorite foods
foods = ["manti", "doner", "cig kofte"]


# Replace the second item with a new one
foods[1] = "kuru pilav"


# Print the list
print(foods)


pause=input('pause')
clear_screen()
'''
#9


Create a tuple with four numbers. Try to change the first number (observe the error)
and then print the tuple.
'''
# Create a tuple with four numbers
nums = (10, 20, 30, 40)


# Try to change the first number
try:
    nums[0] = 99
except TypeError as e:
    print("Error:", e)


# Print the tuple
print("Tuple is still:", nums)




pause=input('pause')
clear_screen()
'''
#10


Create a dictionary representing a student (name, age). Update the age. Create a list of
favorite numbers and add a new number.
'''
student = {
    "name": "Omer",
    "age": 21
}


# Update the age
student["age"] = 22


# Create a list of favorite numbers
favorite_numbers = [9, 25, 1905]


# Add a new number
favorite_numbers.append(42)


print("Student:", student)
print("Favorite numbers:", favorite_numbers)


pause=input('pause')
clear_screen()
'''
#11


Ask the user to input their favorite quote. Save it to a file quotes.txt
and read it back to print it.
'''
# Favorite quote
quote = input("Enter your favorite quote: ")


# Save it to quotes.txt
with open("quotes.txt", "w") as f:
    f.write(quote)


# Read it back
with open("quotes.txt", "r") as f:
    saved_quote = f.read()


print("You entered:", saved_quote)


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
numbers = []


for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)


print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


pause=input('pause')
clear_screen()


'''
Numbers: [1905.0, 25.0, 9.0, 45.0, 11.0]
Sum: 1995.0
Average: 399.0
'''