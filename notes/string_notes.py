# LM 6th String Notes

print("I did it!")

#1 What makes something a string?
    # A string in a collection of symbols held together by quotation marks. Strings are the only data type that allows you to use letters. Quotation marks on either side have to be the same.
#Examples of strings
name = input("What is your name:\n").strip().upper().lower().capitalize().title()

first_name = input("What is your first name:\n").strip().title()

last_name = input("What is your last name:\n").strip().title()

full_name = first_name + " " + last_name

sentence = "The quick brown fox jumps over the lazy dog."

print("Welcome to my program", name)

#2 Why do we have strings?
    # They are the only data type that allows you to use letters.

#3 How do stupid proofing and sanitization relate to each other?
    # Where you take the input and clean it up

#4 What is debugging?
    # debugging is fixing problems in my code. A bug is anything in your code that keeps it from running or making it run proporley.
        # Syntax Error - Miss spelling a variable, or not finishing off the code the way you started it. Ex- string = 'This is my string."
        # Logic Error - Where your code does something you didn't mean for it to do. 
        # Run-Time Error - When there is a problem in the code that will break the code when you try to run it. Ex - letter = "a" int(letter)

#5 How do you debug the different types of errors?
    # You fix the error manually

#6 Describe what each of the methods below does:
    #a find() -  returns the index number of the particular leter
print(sentence.find("brown"))
print(sentence[10:15]) #slice
    #b concatenate (add) - adds string together
    #c upper() - turns the whole code into uppercase letters
    #d lower() - turns the code into lowercase letters.
    #e strip() -  gets rid of all the extra spacings before and after a code.
    #f capitalize() - turns the first letter of code into a capital.
    #g title() - will capitalize the first name and last name in your code.