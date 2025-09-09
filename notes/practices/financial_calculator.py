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
      
      

#What is your monthly income: 3000

#What is your monthly rent/mortgage: 1200

#What is your monthly utilities: 200

#What is your monthly groceries: 250

#What is your monthly transportation: 500\

#Your rent is $1200.00 and that is 40% of your income.

#Your utilities are $200.00 and that is 7% of your income.

#Your groceries are $250.00 and that is 8% of your income.

#Your transportation is $500.00 and that is 17% of your income.

#You should save $300.00 a month, that is 10% of your income.

#You have $550.00 of spending money each month! 
