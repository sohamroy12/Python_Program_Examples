while True:
    name = input("What is your Name: ")
    print(name.capitalize())

"""--------------------------------------------------------------------------------------"""

countries = []
while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)

country = "Italy"

"""--------------------------------------------------------------------------------------"""

while True:
    match country:
        case "Italy":
            print("Ciao")
        case "USA":
            print("Hello")
        case "Germany":
            print("Hallo")
    break

members = ["john", "sarah", "dora"]

for i in members:
    y = i.capitalize()
    print(y)

print(members)

print(lambda i : i.capitalize() in members)

# file = open("essay.txt", 'r')
# read = file.read()
# print(read.upper())

"""--------------------------------------------------------------------------------------"""

"""
The zip() Function
In the coding area, we have defined two lists. 
Each country in the first list should be written in a new file corresponding to the name in the filenames list. 
So, "Albania" should be written in a new a.txt file, "Belgium" in a new "b.txt" file and so on.
"""

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for countrie, filename in zip(countries, filenames):
    file = open(filename, 'w')
    file.write(countrie)
    file.close()

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

"""--------------------------------------------------------------------------------------"""

# Creating Multiple Text Files
# In the coding area, we have defined a list of countries. Add some code that uses a for loop to generate a text file for each country (e.g., "Albania.txt", "Belgium.txt", and so on).
# Each file should have its country name as content (e.g., Albania.txt has Albania as content).

for countrie in countries:
    file = open(f"{countrie}.txt", 'w')
    file.write(countrie)
    file.close()

"""--------------------------------------------------------------------------------------"""

"""
Coding Exercise: Adding to Text File
Please code this exercise in your computer IDE, so you gain experience with working with text files in a local IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:
1. prompts the user to enter a new member.
2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
In the above example, Solomon Right will be added to members.txt updating the content of the file to:
John Smith
Sen Lakmi
Sono Octonot
Solomon Right
"""
new_member = input(f"Please input a New Member: ")

file_r = open('members.txt', 'r')
members = file_r.readlines()
file_r.close

members.append(new_member + "\n")

file_w = open('members.txt', 'w')
members =file_w.writelines(members)
file_w.close()

"""--------------------------------------------------------------------------------------"""

"""
Coding Exercise: Generate Multiple Text Files
Open your computer IDE and place the following in a Python file:

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

Then, create a program that:

1. generates multiple text files by iterating over the filenames list,

2. and writes the text Hello  inside each generated text file.
"""

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for files in filenames:
    file = open(files, 'w')
    file.write("Hello")
    file.close()

"""--------------------------------------------------------------------------------------"""

"""
Coding Exercise: Reading Multiple Files
Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

Then, create a program that:

1. reads each text file and

2. prints out the content of each file in the command line.

The expected output would be like the following:
I am a
I am b
I am c
"""

filenames = ['a.txt', 'b.txt', 'c.txt']

for files in filenames:
    file = open(files, 'r')
    read = file.readline()
    print(read)

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

file = open("data.txt", 'w')
 
file.writelines("100.12\n")
file.writelines("111.23\n")
 
file.close()

"""--------------------------------------------------------------------------------------"""

"""
List Comprehension
We have defined a list of strings in the coding area. Your task is to add some code that:
(1) uses list comprehension to capitalize all the names and surnames of the list, and
(2) prints the updated list
The output of your code should be as below:
['John Smith', 'Jay Santi', 'Eva Kuki']
"""

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

"""--------------------------------------------------------------------------------------"""

"""
Length and List Comprehension
Extend the given code so the code prints out a list containing the number of characters for each username.
The output of your code should be as below:
[9, 11, 11]
"""
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)

"""--------------------------------------------------------------------------------------"""

"""
Type Conversion and List Comprehension
The coding area contains a list of numbers, each stored as a string. Your task is to add some code that:
(1) converts the numbers from strings to floats, and
(2) prints out the updated list.
The output of your code should be as below. Notice the numbers are floats without quotes.
[10.0, 19.1, 20.0]
"""
user_entries = ['10', '19.1', '20']
user_entries = [float(ue) for ue in user_entries]
print(user_entries)

"""--------------------------------------------------------------------------------------"""

"""
List Comprehension on Numbers
We have defined a numbers variable in the coding area. Add some code that:
(1) multiplies each number of the list by 2, and
(2) prints out the updated list.
Here is the expected output:
[20, 40, 60]
"""
numbers = [10, 20, 30]
numbers = [n*2 for n in numbers]
print(numbers)

"""--------------------------------------------------------------------------------------"""

"""
Sum of Numbers
Extend the given code so it prints out the sum of the numbers. Note that the numbers are currently string types.
The output of your code should be as below:
49.1
"""
user_entries = ['10', '19.1', '20']
user_entries = sum([float(n) for n in user_entries])
print(user_entries)

"""--------------------------------------------------------------------------------------"""

"""
With Context Manager -File Reading
The code in the coding area successfully reads and prints out the content of the bear.txt file. 
Your task is to rewrite the code by using a "with" context manager to achieve the same thing.
"""

with open("todos.txt", "r") as file:
    content = file.read()    
print(content)

"""--------------------------------------------------------------------------------------"""

"""
With Context Manager -Analyzing Content
The code in the coding area successfully reads and prints out the number of characters in the bear.txt file. 
Similar to the previous task, your task is to rewrite the code by using a "with" context manager to achieve the same thing.
"""

with open("essay.txt", 'r') as file:
    content = file.read()
nr_chars = len(content)
print(nr_chars)

"""--------------------------------------------------------------------------------------"""

"""
With Context Manager -File Writing
The code in the coding area creates a new file.txt file and writes the text snail inside the file.
Your task is to rewrite the code by using a with-context manager.
"""

with open('file.txt', 'w') as file:
    file.write('snail')

"""--------------------------------------------------------------------------------------"""

"""
With Context Manager and For-Loop
In the coding area, we have defined a list of languages. Add some code that:
(1) iterates over the list using a for-loop,
(2) creates a new text file in each iteration using a with-context manager,
(3) each file should be named according to the current item (i.e., English.txt, German.txt, and Spanish.txt).
(4) the content of each file should be the item of the list (e.g., the content of the file English.txt should be English).
"""

"""--------------------------------------------------------------------------------------"""
languages = ['English', 'German', 'Spanish']

for lang in languages:
    with open(f"{lang}.txt", "w") as file:
        file.write(f"{lang}")

"""--------------------------------------------------------------------------------------"""

"""
With Context Manager with Reading and Writing
In the coding area there is a story.txt file tab that contains some text.
Your task is to make a copy of the story.txt file. Here are the exact steps:
(1) Read the story.txt file using a with-context manager and store its text in a string variable.
(2) Create a new story_copy.txt file using a second with-context and write the string variable in the file.
"""
with open('story.txt', 'r') as file:
    Str = file.read()
with open('story_copy.txt', 'w') as file:
    file.write(Str)

"""--------------------------------------------------------------------------------------"""

"""
FAQ
Q1: When should I use read() and when readlines()?
A: If you want to get all the text as one single string, use read(). 
If you want to get separate strings for each line, use readlines().

Q2: How is the with-context manager actually able to close the file when we are not including the close() method?
A: The close() method is called implicitly even though we don't call it explicitly. 
The Python interpreter will call the method when it sees that we have written a with-context manager.
"""

"""--------------------------------------------------------------------------------------"""

"""
Advanced Password Validation
Write a program that: 
(1) asks users to enter a password,
(2) returns "Great password there" if the password has more than 7 characters,
(3) returns "Password is OK, but not too strong" if the password has exactly 7 characters,
(4) returns "Your password is weak" if the password has 7 or fewer characters.
"""

passw = input("Enter a new password: ")

if len(passw) > 7:
    print("Great password there!")
elif len(passw) ==7 :
    print("Password is OK, but not too strong")
else :
    print("Your password is weak")

"""--------------------------------------------------------------------------------------"""

"""
Percentage Calculator with Error Handling
Take a look at the code in the coding area. You should expand that code. Your task is to:
(1) calculate the percentage using the  value/total * 100 formula
(2) print out the message "That is 40.0%" (or whatever the calculated percentage value is)
(3) If the user doesn't enter a number but a string (e.g., hi) for the total value or the value, the program should print out the message shown in the screenshot below:
"""
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    
    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")
except SyntaxError as x:
    print("{x}")

"""--------------------------------------------------------------------------------------"""

"""
Advanced Error Handling
As you might know, it is not mathematically possible to divide a number by zero. Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

>>> 20 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
With that in mind, your task for this exercise is to extend the program you created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value".
"""

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    
    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")
except ZeroDivisionError:
    print("Your total value, cannot be a Zero")

"""--------------------------------------------------------------------------------------"""

"""

For Loops and Conditionals 1
Your task for this exercise is to:
(1) loop over the colors items
(2) print out the item in every loop if the item is greater than 50.
In other words, the output of your program would be:
98
54
54
"""
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color > 50:
        print(color)

"""--------------------------------------------------------------------------------------"""

"""
For Loops and Conditionals 2
Your task for this exercise is to:
(1) loop over the passwords list and
(2) print out only those passwords that are less than 8 characters.
"""
passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]
for password in passwords:
    if len(password) < 8:
        print(password)

"""--------------------------------------------------------------------------------------"""

"""
Loops and Slicing
In the coding area we have defined a list of filenames. Your task is to:
(1) loop over the list
(2) print out the filename of each item without the extension using slicing.
The output of your program would look like this:
report
downloads
success
folders
"""

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for file in filenames:
    if file.endswith(".txt"):
        file = file[:-4]
        print(file.capitalize())

"""--------------------------------------------------------------------------------------"""

"""
Loops, Slicing, and String Manipulation
This exercise is similar to the previous one but with an added feature. In the coding area we have defined a list of filenames. Your task is to:
(1) loop over the list
(2) print out the filename of each item without the extension using slicing and with the first letter capitalized.
The output of your program would look like this:
Report
Downloads
Success
Folders
"""
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for file in filenames:
    if file.endswith(".txt"):
        file = file[:-4]
        print(file.capitalize())

"""--------------------------------------------------------------------------------------"""

"""
Function to Process a List 1
Complete the function given in the coding area. The function should:
(1) calculate the maximum value of the grades list,
(2) return the calculated value.
After completing the function definition you should call the function and print out its output.
The output of your code would be:
9.7
"""
def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grades = (max(grades))
    return max_grades
print(get_max())

"""--------------------------------------------------------------------------------------"""

"""
Function to Process a List 2
The get_max function you created in the previous exercise returned 9.7. 
In this exercise, you should:
(1) change the function so this time it returns the following string:
"Max: 9.7, Min: 9.2"
where 9.7 is the maximum, and 9.2 is the minimum.
Note: For the exercise to be marked as correct by the system, you should return the exact string "Max: 9.7, Min: 9.2"
"""
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    # Return the message string
    return message
    
print(get_max())

"""--------------------------------------------------------------------------------------"""

"""
Function to Process a String
Your task for this exercise is to:
(1) define a function named format_filename
(2) define a variable named filename inside the function
(3) assign the string "report.txt" to filename
(4) remove the last four characters (.txt) from the filename string and capitalize its first letter.
(5) return the altered string.
(6) call the function and print out its output.
"""
def format_filename():
    filename = 'report.txt'
    filename = filename[:-4].capitalize()
    return filename

print(format_filename())

"""--------------------------------------------------------------------------------------"""

"""
Function to Process a Number
Your task for this exercise is to:
(1) define a function named square_number
(2) define a variable named number inside the function
(3) assign the integer 5 to number
(4) raise number to the power of 2 and store the result in a result variable.
(5) return the result variable.
(6) call the function and print its output
"""
def square_number():
    number  = int(5)
    result  = number ** 2
    return result 

print(square_number())

"""--------------------------------------------------------------------------------------"""

"""
Liters Converter Function
Your task for this exercise is to:
(1) define a function named liters_to_m3
(2) the function should take a liters parameter
(3) in the function you should converts liters to cubic meters (1000 liters = 1 cubic meters)
(4) then, return the cubic meters.
Note: Defining the function is enough. 
      You do not need to call or print out a function output, but you should name the function exactly liters_to_m3.
"""
def liters_to_m3(liters):
    cubic = float(liters) / 1000
    return cubic

"""--------------------------------------------------------------------------------------"""

"""
Password Validation Function
Complete the strength function. The function will check the strength of a given password. Specifically, the function should:
(1) get a password argument
(2) return the string "Strong Password" if all of the following conditions are true:
Password is 8 or more characters
Password has at least one uppercase letter
Password has at least one digit.
(3) if one or more of the above conditions are not met, the function should return "Weak Password".
Note:  You can make use of the code we developed in the Bonus Example on Day 9.
"""
def strength(password):
    result = {}
 
    # Check the length of the password
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
 
    # Check if the password contains a digit and an uppercase letter
    digit = False
    uppercase = False
 
    # Iterate over each character in the password
    for i in password:
        # Check if the character is a digit
        if i.isdigit():
            digit = True
        # Check if the character is an uppercase letter
        if i.isupper():
            uppercase = True
 
    # Store the results in the dictionary
    result["digits"] = digit
    result["upper-case"] = uppercase
 
    # Check if all the strength attributes are True
    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"

"""--------------------------------------------------------------------------------------"""

"""
Average Function
Define a function that:
(1) takes a list as an argument
(2) returns the average value of the list items.
For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.
Note: You can name the function anyway you want. It's enough to define the function. There is no need to call it.
"""
def foo(items):
    avg_value = sum(items)/len(items)
    return avg_value
"""--------------------------------------------------------------------------------------"""
"""
Greeting Function
Define a function that:
(1) takes a person's name as a parameter
(2) greets the person with Hi Person.
For example, if I call your function using foo("lisa") the function should return Hi lisa .
"""
def foo(Name):
    call = f"Hi {Name}"
    return call

"""--------------------------------------------------------------------------------------"""
"""
Concatenation Function
Implement a function that:
(1) takes two strings as parameters,
(2) concatenates the strings
(3) returns the concatenated string.
For example, if I called your function with foo('hello', 'hi') it would return hellohi.
"""

def foo(item1, item2):
    item = item1 + item2
    return item

"""
Greeting Function and String Manipulation
Implement a function that:
(1) takes a person's name (e.g. 'john') as a parameter
(2) returns a greeting (e.g. Hi John)
Note that the first letter of the person's name should be capitalized by the function.
"""

def foo(name):
    return f"Hi {name.title()}"

"""--------------------------------------------------------------------------------------"""
"""
Age Function
Define a function named get_age  which:
(1) has two parameters, year_of_birth and current_year
(2) the current_year  parameter should be a default parameter
(3) the default value of current_year should be the current year (e.g., the integer 2025)
(4) the function should calculate and return the age of the user given the year_of_birth and the current_year.
"""
def get_age(year_of_birth, current_year=2025):
    current_age = int(current_year) - int(year_of_birth)
    print(current_age)
    return current_age

get_age(1993, 2025)
"""--------------------------------------------------------------------------------------"""
"""
Split Function
Write a get_nr_items function that:
(1) gets as a parameter one string with commas (e.g., "john,lisa, teresa")
(2) the function calculates the number of words (i.e., three words in the above example)
(3) returns the number of words.
For example, if I called your function with get_nr_items("john,lisa, teresa") it would return 3.
"""

def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)
    
get_nr_items("john,lisa, teresa")
"""--------------------------------------------------------------------------------------"""
"""
Square Area Function
Define a function that:
(1) takes the side length of a square as a parameter
(2) calculates and returns the area of a square.
For example, if I was to call your function with foo(7)it would return 49.  You can name the function anyway you want.
"""
def square(length):
    area = length * length
    return area
    
square(7)

"""--------------------------------------------------------------------------------------"""

"""
Temperature Checker
Define a function that:
(1) takes a temperature as a parameter
(2) returns "Warm" if the temperature is greater than 7
(3) returns "Cold" if the temperature is equal to or less than 7.
If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold and so on.
"""
def temperature(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"
    
temperature(9)

"""--------------------------------------------------------------------------------------"""

"""
Password Length Checker
Define a function that:
(1) takes a string as a parameter
(2) returns False if the string contains less than 8 characters
(3) returns True if the string contains 8 or more characters
In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.
"""
def strength(password):
    # Check the length of the password
    if len(password) >= 8:
        return True
    else:
        return False

strength("mylongpassword")
"""--------------------------------------------------------------------------------------"""

"""
Water State Checker
Define a  water_state function that:
(1) gets a temperature parameter
(2) returns the string "Solid" if the temperature is less than or equal to 0
(3) returns "Liquid" if the temperature is greater than 0, but less than 100.
(4) returns "Gas" if the temperature is greater than or equal to 100.
"""

def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
"""--------------------------------------------------------------------------------------"""

"""
Water State Checker Advanced
In the previous exercise, we hardcoded the values 0 and 100. However, it is better to place those values in constants. Therefore, your task is to:
(1) create a FREEZING_POINT and a BOILING_POINT variable outside of the water_state function and store the values 0 and 100 in them respectively.
(2) modify the function of the previous exercise by using the variables given above instead of the hardcoded 0 and 100 values. The previous function is provided in the coding area.
"""
FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"

"""--------------------------------------------------------------------------------------"""

"""
Advanced Temperature Function
Define a function that:
(1) takes temperature as a parameter
(2) returns "Hot" if the temperature is greater than 25
(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
(4) returns "Cold" if the temperature is less than 15.
If I called your function with foo(10) it would return "Cold". 
Calling it with foo(15), foo(16), or foo(25) would all return "Warm". Calling it with foo(26) would return "Hot".
"""
def temp(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    else:
        return "Cold"

"""--------------------------------------------------------------------------------------"""

"""
Coding Exercise 2
Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters. 
For example, I was to call your function with foo(1) I would get an output of 29.57353. 
If I called it with  foo(5) I would get 147.86765, and so on.
"""
def convert(ounce):
    ounce = float(ounce)
    ml = ounce * 29.57353
    return ml

"""--------------------------------------------------------------------------------------"""

"""
Coding Exercise 1
Your task for this exercise is to add an Exit button that quits 
the program and apply a black theme to the program you built-in yesterday's coding exercise.


"""


# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from converters import convert

sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()

"""--------------------------------------------------------------------------------------"""

