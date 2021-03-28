"""
CP1404 - prac_04 - list_exercises
Cameron Attard
"""


# 1 Basic list operations

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is {}".format(numbers[0]))
print("The last nuymber is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

# 2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Username: "))
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
