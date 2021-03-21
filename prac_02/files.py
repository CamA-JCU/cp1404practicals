# 1. Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.

open_file = open("name.txt", 'w')
name = str(input("Name: "))
print(name, file=open_file)
open_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

open_file = open("name.txt", 'r')
name = open_file.read().strip()
print("Your name is", name)

# 3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together
# then prints the result, which should be... 59.

open_file = open("numbers.txt", 'r')
number1 = int(open_file.readline())
number2 = int(open_file.readline())
print(number1 + number2)
open_file.close()

# 4. Now write a fourth block of code that prints the total for
# all lines in numbers.txt or a file with any number of numbers.

total = 0
open_file = open("numbers.txt", 'r')
for line in open_file:
    number = int(line)
    total += number
print(total)