# LM Updated Financial Calculator 

def clean(info):
    return float(input(f"What is your monthy {info}"))

def money(info, income):
    return info / income * 100

income = clean("income")
morgage = clean("rent/morgage")
utilities = clean("utilities")
groceries = clean("groceries")
transportation = clean("transportation")

savings = income * .1

total = income - (morgage + utilities + groceries + transportation + savings)

print(f"Your rent is: $", morgage, "and that is", money(morgage, income),"% of your income")
print(f"Your untilities are: $", utilities, "and that is", (utilities, income), "% of your income")
print(f"Your groceries are: $", groceries, "and that is", (groceries, income), "% of your income")
print(f"your transportation is: $", transportation, "and that is",(transportation, income), "% of your income")
print(f"Your savings: $", savings, "and that is", income * .1, "% of your income" )
print(f"Your spending amount is: $", total)

