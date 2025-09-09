# LM 6th String Notes

print("I did it!")

#1 What makes something a string?
    # A string in a collection of symbols held together by quotation marks. Strings are the only data type that allows you to use letters. Quotation marks on either side have to be the same.
#Examples of strings
name = input("What is your name:\n").strip().upper().lower().capitalize().title() # ".strip" gets rid of all the extra spacings before and after a code. 
# ".upper" turns the whole code into uppercase letters. "lower" turns the code into lowercase letters. "capitalize" turns the first letter of code into a capital. "title" will capitalize the first name and last name in your code.
first_name = input("What is your first name:\n").strip().title()

last_name = input("What is your last name:\n").strip().title()

full_name = first_name + " " + last_name

sentence = "The quick brown fox jumps over the lazy dog."

print("Welcome to my program", name)

#2 Why do we have strings?
    #

#3 How do stupid proofing and sanitization relate to each other?
    #

#4 What is debugging?
    # debugging is fixing problems in my code.
        # Syntax error
        # logic error
        # run time error
#5 How do you debug the different types of errors?
    #

#6 Describe what each of the methods below does:
    #a find()
    #b concatenate (add)
    #c upper()
    #d lower()
    #e strip()