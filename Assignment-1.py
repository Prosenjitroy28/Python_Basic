''' 
Q1. Simple Calculator Program (25 Marks)
Write a Python program that performs basic arithmetic operations.
A. Input & Setup (10 marks)
1.  Ask the user to input two numbers. (4 marks)
2. Convert both inputs into integers or floats. (6 marks)
B. Calculations (10 marks)
Compute and print the following:
1. Addition (2 marks)
2. Subtraction (2 marks)
3. Multiplication (2 marks)
4. Division (2 marks)
5. Clearly labeled outputs (2 marks)
C. Code Style (5 marks)
1. Use comments to explain your steps. (3 marks)
2. Use proper spacing/indentation. (2 marks)
Q2. User Introduction Program (20 Marks)
Create a Python program that collects user information and prints an introduction sentence.
A. Inputs (10 marks)
Ask the user for:
1. Name (3 marks)
2. City (3 marks)
3. Favourite hobby (4 marks)
B. Output (8 marks)
Print a sentence such as:
Hello Sazzad! You live in Dhaka and you enjoy running.
- Correct use of string concatenation or f-string (4 marks)
- Output formatting and clarity (4 marks)
C. Code Quality (2 marks)
Comments, readability, etc.
Q3. Temperature Converter (20 Marks)
Write a program to convert Celsius to Fahrenheit.
A. Input (5 marks)
1. Take temperature in Celsius from the user. (2 marks)
2. Convert to float. (3 marks)
B. Calculation (10 marks)
Use the formula:
F = (C * 9/5) + 32
- Correct formula implementation (6 marks)
- Correct variable usage (4 marks)
C. Output (5 marks)
Print Fahrenheit with a message:
Temperature in Fahrenheit is: 77.0°F
- Correct formatting (3 marks)
- Clear message (2 marks)
Q4. Billing Program (20 Marks)
Write a program that calculates a shopping bill.
A. Inputs (10 marks)
Ask the user for:
1. Item name (3 marks)
2. Price (3 marks)
3. Quantity (4 marks)
B. Calculation (6 marks)
Compute:
Total = price × quantity
- Correct arithmetic (4 marks)
- Correct variable handling (2 marks)
C. Output (4 marks)
Print a bill like:
Total Bill for Notebook = 120
- Output formatting (2 marks)
- Clear labeling (2 marks)
Q5. Student Information Card (15 Marks)
Create a simple program that prints a formatted “Student ID Card”.
A. Input (6 marks)
Ask the user for:
1. Student Name (2 marks)
2. Class and Section (2 marks)
3. School Name (2 marks)
B. Formatting (7 marks)
Use print(), newlines \n, or multi-line strings to display something like:
----- STUDENT ID CARD -----
Name: Kazi Nazrul Islam
Class: 8B
School: Dhaka Residential Model College
----------------------------
- Alignment, spacing, and formatting (4 marks)
- Use of f-string or concatenation (3 marks)
C. Code Quality (2 marks)
Comments + clean formatting.
'''

'''
Q1. Simple Calculator Program
Write a Python program that performs basic arithmetic operations.
'''
#Ask the user to input two numbers And convert both inputs into floats
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

#Performs basic arithmetic operation:
addition=a+b  #Additon of two numbers
subtraction=a-b  #Subtraction of two numbers
multiplication=a*b  #Multiplication of two numbers
division=a/b  #Division of two numbers

#Print result:
print("Results:")
print("Additon of two numbers:",addition)
print("Subtraction of two numbers:",subtraction)
print("Multiplication of two numbers:",multiplication)
print("Division of two numbers:",division)



'''
Q2. User Introduction Program
Create a Python program that collects user information and prints an introduction sentence.
'''

#Ask user for name,city and favourite hobby:
name=input("Enter your name:")
city=input("Enter your city:")
hobby=input("Enter your favourite hobby:")

#Printing sentence using f-string:
print(f"Hello {name}! You live in {city} and you enjoy {hobby}.")


'''
Q3. Temperature Converter
Write a program to convert Celsius to Fahrenheit.
'''
#Take temperature in celsius from user and conver to float:
temperature=float(input("Enter the temperature in celsius:"))

#Convert celsius to fahrenheit using this F=(C*9/5)+32 formula:
fahrenheit=(temperature*9/5)+32  #calculation

#Output:
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")



'''
Q4. Billing Program
Write a program that calculates a shopping bill.
'''
#Ask user for item name,price,quantiy,calculation:
item_name=input("Enter item name:")
price=int(input("Enter item price:"))
quantity=int(input("Enter item quantity:"))

#Bill calculation:
total_bill=price*quantity

#Output using f-string:
print(f"Total Bill for {item_name} = {total_bill}")



'''
Q5. Student Information Card
Create a simple program that prints a formatted “Student ID Card”.
'''
#Ask the user for Student Name,Class and Section,School Name:
student_name=input("Enter student name:")
class_section=input("Enter class and section")
school_name=input("Enter school name:")

#formatting using multiline string and fstring:
student_id_card=f"""----- STUDENT ID CARD -----
Name: {student_name}
Class: {class_section}
School: {school_name}
----------------------------
"""

#output:
print(student_id_card)

