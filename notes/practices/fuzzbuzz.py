# LM 6th FuzzBuzz 

i = 1

while i < 50:
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")

    else:
        print(f"{i}")
    i += 1