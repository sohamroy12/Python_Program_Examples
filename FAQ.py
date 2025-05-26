"""
FAQ
Q1: In the app, we imported functions.py from main.py. Is it possible to import main.py from functions.py?
A: Yes, that is technically possible. You can do import main in functions.py. However, that import doesn't make much sense. We usually import the backend to the frontend. The backend is the script where the processing is done (i.e., reading and writing the to-do files), and the frontend is the code that constructs the user interface (i.e., the command line).

Q2: Can we import more than one .py file from the main.py file?
A: Yes, that is possible, and as the program expands, it is recommended to create more backend files, and you can import all those files from main.py. For example, you might want to create some functions which send out the to-do items by email to your email address. You might also want to create some functions that produce a PDF with the to-do items inside. It is recommended to write the email and the PDF functions in separate modules and then import those modules from the main module. For example, if we had these files:

main.py
functions.py
pdf.py
email.py
In main.py we would have these lines:

import functions
import pdf
import email

FAQ
Q1: I want to give the app to someone else to use it, but that person does not have Python installed. How can that person use the app?
A: You need to convert the .py file into an .exe (for Windows users), an .app file (for Mac users) or a .deb file (for Linux users). 
You will learn how to do that on Day 18.

Q2: The GUIs we are building work only as desktop programs. How can we make a web app?
A: FreeSimpleGUI is only able to create desktop GUIs. To make web apps, you need to use a Python web framework. 
The most popular web frameworks are Django, Flask, and Streamlit. 
In fact, Python is way better for building web apps. We will eventually build a Todo List web app on Day 19.


Question 1:
What is Text in the following code?
sg.Text
A: Yes, "Text" is a type. Usually, types start with an upper case letter.
    You selected "Type" as the correct answer because "Text" in the code represents a data type, which typically starts with an uppercase letter, distinguishing it from instances or functions that follow different naming conventions. 
    This distinction is fundamental in programming, reinforcing your understanding of how data types are categorized.

Question 2:
What is Text("Welcome") in the following code?
sg.Text("Welcome")
A: Yes, Text("Welcome") is an instance of Text.

FAQ
Q1: I get a numpy error when I try to install streamlit.

A: Open the PyCharm Terminal and execute these commands one by one:

pip uninstall numpy

pip install numpy==1.21.1

Then, close the terminal, open it again, and try to start the streamlit app again:

streamlit run main.py.

Your streamlit app should now run normally.



Q2. I always thought that in order to code a website, one needs to use HTML. So how comes we did not use any HTML in our app?

A: It is true that every webpage is built on top of HTML code. However, in our case, Streamlit prepares the HTML code from the Python code we wrote in the web.py file and renders that HTML in the browser. In other words, Streamlit acts as a converter tool that converts Python to HTML.



Q3: Are there alternatives to Streamlit for building websites with Python?

A: Yes. Streamlit is one of the Python web frameworks. Other popular frameworks are Flask and Django. You will learn Flask and Django in this course.



Q4 Which is the best web framework for Python?

A: There is no "best" framework. As a programmer, you should choose the best framework that suits your use case. For example, Streamlit has the advantage that it is easier to use but has limitations. That makes Streamlit an ideal choice for small apps. On the other hand, Flask is an excellent choice for medium apps, and Django is considered the best for building larger web apps such as news websites, e-learning platforms, etc.



Q5: We are creating a virtual environment and installing packages every time we create a new PyCharm project, but my computer disk space is low. Is there a way to save disk space?

A: It is a good practice to create a virtual environment for every project, but it is not a must. If you have low hard disk space, you can tell PyCharm to use the global Python interpreter whenever you create a new project. That way, you will not need to reinstall packages for every project since every project will use the same global interpreter.

To make PyCharm use the Python global interpreter, follow these steps:

1. When you are creating a PyCharm project, select the Previously configured interpreter option and click on Add Interpreter and then on Add Local Interpreter...




2. In the next window, select System Interpreter and then select one of the global interpreters (e.g., Python 3.11) you have installed. Press OK to finish and continue with the next project creation steps as normal.



"""