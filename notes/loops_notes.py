# LM 6th Time and Four Loops Notes

import datetime

current = datetime.datetime.now()
hour = current.hour

# print(f"The time in seconds since Jan 1, 1970: {epoch}")

print(f"The time is: {current}")
print(f"The hour is: {hour}")

# What is a loop? 
    # keeps going until a specific condition is met.

# What are the two types of loops?
    # 1 - For Loop - for (Variable) in (Variables)
    # 2 - While loops - infinite loops

# What is iteration
    # keeps track of how many times the loop has run. Snap shot, pauses the loop so you can look at it.

# 1 interator (Keep track of loop number)
# 2 end condition (tells the loop by step)
# 3 incrase the iterrator

# What are lists? 
    # Allows you to store multiple peices of information within the same variables.

siblings = ["Rachel", "Sarah", "Abby", "Caleb", "Lily", 29, 27, 24, 20, 16]

print(siblings[3])
print(siblings)
siblings[4] = "Tia"
siblings[6] = "Xavier"
siblings.remove("Lily")
print(siblings)

# How do you make lists in python? 
    # surrounded by straight brackets[]. Every item in the list must be a proper data type.

# How do you make for loops in python? 
for sibling in siblings: # This code olny works when put after the example - siblings = ["Rachel", ect.,.]
    print(f"Hello {sibling}")

# How do you make while loops in python?

# bad example of while loop - while True: # This code only workds when put after the example - siblings = ["Rachel", ect.,.]
#          print("Oh No!")

# Good While Loop
i = 1

while i < 21:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1

import random

number = random.randint(1,20)
x = 1
while x != number:
    print("Duck")
    x += 1

print("Goose!")

while True:
    if number == x:
        print("Goose!")
        break # breaks the loop( whithout this the "Duck" would repeat)
    else:
        print("Duck")
        x += 1
