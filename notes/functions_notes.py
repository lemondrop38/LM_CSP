# LM 6th Functions Notes

# What a function is
    # a function is a set of instructions that are executed when you call on a key word. 

# Why we use functions
    # use functions to save space in the code.

# How to write a function in Python
    # "f" is a string that allows you to use curly brackets) Everything repeated must match perfectly or the code will break.

def welcome():
    name = input("what is your name\n")
    print(f"Hello {name}!")
    
print(f"The function is over!")

welcome() # this is called calling the fucntion
welcome()
welcome()
welcome()
welcome()
welcome()


def add(numer): # parameters are given when the function is defined
    num_one = num_one + num_two
    print(num_one)

num_one = 12
num_two = 14
add(num_one) # Arguements are given when we call the function
add(4,6)
add(60, 50)

# What parameters and arguments are
    # parameters are given when the function is defined, arguemnts are given when we call the function.

# How to use parameters and arguments in python
    # parameters go inside the parenthese when you define the function.

# What return statements are
    # are going to take what happens inside the function and puts it back to where you originally called the function.

# How to use return statements in a program

def clean(info):
    return info.strip().lower()

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print(f"Hello, {clean(name)}. I have heard you are trying to {clean(quest)}, that is super cool! Are you sure {clean(color)}. is your favorite color?")
