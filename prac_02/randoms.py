import random
print(random.randint(5, 20))  # line 1
#   for line 1 i got 7
#   the smallest number i could have seen is 5 and the largest 20
print(random.randrange(3, 10, 2))  # line 2
#   for line 2 i got 9
#   the smallest number i could have seen is a 3 and the largest 9.
#   Line 2 could not produce 4 as it has an incremental of 2 from 3.
print(random.uniform(2.5, 5.5))  # line 3
#   for line 3 i got 4.161715623794262
#   the smallest number is 2.5 and largest 5.5 floating point.


#   produce random  number between 1 and 100 inclusive
print(random.randint(1,100))