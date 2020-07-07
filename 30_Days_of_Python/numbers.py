# DAY 2

# Data type

# ------------------------------------ #
# Numbers

# int
# float
# complex (not used commonly)

num1 = 100
print(type(num1))   # <class 'int'>

num2 = 99.99
print(type(num2))   # <class 'float'>

expression1 = num1 * 10
print(type(expression1))    # <class 'int'>

expression2 = num1 + num2
print(type(expression2))    # <class 'float'>

# ------------------------------------ #
# Math functions

print(round(2.1))   # 2
print(round(5.9))   # 6
print(abs(-34))     # 34

# ------------------------------------ #
# Variables

name1 = 'Python'    # string assignment within single quotes
name2 = "Python"    # string assignment within double quotes
name3 = '''This is a a very long string and supports 
            multi-line statements as well'''  # string assignment within 3 single quotes
name4 = 'Hello! \"Rockstar Programmer\"'    # string with escaped character sequence
print(type(name1))   # <class 'str'>
print(type(name2))   # <class 'str'>
print(type(name3))   # <class 'str'>
print(name3)
print(type(name4))   # <class 'str'>
print(name4)

first_name = 'Mike'
last_name = 'Tyson'
print(first_name + ' ' + last_name)     # Mike Tyson

user_name = 'John'
age = 40
print(user_name + str(age))     # John40
print(type(str(age)))    # <class 'str'>

lucky_number = 7
lucky_number_string = str(7)
lucky_number_extracted = int(lucky_number_string)
print(lucky_number_extracted)   # 7
