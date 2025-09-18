# LM 6th Conditional Notes

# What puts something inside of the “if” statement?
    # when its indented bellow it.

num = 12

if num < 10:
    print(f"{num} is a single digit number")

# What do if statements do?
    # check "if" true or false statement.


# What are boolean statements? 
    # the "num < 10:" is an example of the bolleam statement.

# What do else statements do?
    # if its not true we do something else.

else:
    print(f"{num} is not a single digit number")

# What kind of statement do you use if you have more than 2 needed outcomes?
    # elif statement (else if) ex - elif (variable) == ( )

# What do each of the different symbols mean in conditionals?
    # < less than
    # > greater than
    # <= less than or equal to
    # >= greater than or equal to
    # == equal
    # ! not equal

# What are the 3 logical operators?
    # and, or, not

if num >= 0 and num < 10: # and means both must be true
    print(f"{num} is a single difit numner")
elif num < 25 or num == 50: # or means only 1 must be true
    print(f"Wow{num} is a really cool number!")
elif not num < 100: # not means takes whatever it is and does the opposite
    print(f"{num} is a large number")
else:
    print(f"You typed in a {num}")

# What are logical operators for?
    # they allow us to check two or more conditions at the same time.

# What does a nested conditional statement do?
    # inside of the condition yo can have another condition.

name = input("Please tell me your name:")
if name == "Lily":
    print("You are the student!")
    if num == 4:
        print("That is my favorite number!")
elif name == "Tia" or name == "Andrew":
    print("You are TA's!")
else:
    if name == "Lucas":
        print("You have a cool name!")

