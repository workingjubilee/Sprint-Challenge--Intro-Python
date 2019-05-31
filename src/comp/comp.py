# The following list comprehension exercises will make use of the
# defined Human class.
import math
import re
import string


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i.name for i in humans if re.match(r'D', i.name)]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [i.name for i in humans if re.search(r'e$', i.name)]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [i.name for i in humans if re.match(r'C|D|E|F|G', i.name)]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age+10 for i in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{i.name}-{i.age}' for i in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(i.name, i.age) for i in humans if 32 >= i.age >= 27]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.


def embiggen(human):
    bigger_name = human.name.upper()
    bigger_age = human.age + 5
    return Human(bigger_name, bigger_age)


print("All names uppercase:")
g = [embiggen(i) for i in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(i.age) for i in humans]
print(h)
