name=input("Enter your name:")

Monthly_income=float(input("enter your income:"))

Rent=int(input("enter rent:"))

Food_expenses=float(input("enter food_expenses:"))

travel_cost=float(input("enter travel cost:"))

Entertainement_cost=float(input("enter entertainment cost:"))

other_cost=float(input("enter other cost:"))


Total_expenses=Rent+Food_expenses+travel_cost+Entertainement_cost+other_cost

print("nane:",name)
print("Total_expenses:",Total_expenses)
print("monthly_income:",Monthly_income)

remaining_money=Monthly_income-Total_expenses

saving_precentage=(remaining_money/Monthly_income or float('remain'))*100

print("remaining_money:",remaining_money)
print("saving_percentage:",saving_precentage)