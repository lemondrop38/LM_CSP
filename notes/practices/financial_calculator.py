# LM Financial Calculator 

income = float(input("What is your monthy income:\n"))
morgage = float(input("What is your monthy rent/morgage:\n"))
utilities = float(input("what is your monthly untilities:\n"))
groceries = float(input("what is your monthly groceries:\n"))
transportation = float(input("what is your monthly transportation:\n"))

savings = income * .1

total = income - (morgage + utilities + groceries + transportation + savings)

print("Your rent is: $", morgage, "and that is", (morgage / income) * 100,"% of your income")
print("Your untilities are: $", utilities, "and that is", (utilities / income) * 100, "% of your income")
print("Your groceries are: $", groceries, "and that is", (groceries / income) * 100, "% of your income")
print("your transportation is: $", transportation, "and that is",(transportation / income) * 100, "% of your income")
print("Your savings: $", savings, "and that is", (income * .1), "% of your income" )

print("Your spending amount is: $", total)
      
      