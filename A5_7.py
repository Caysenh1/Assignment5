MealCost = float(input("Enter Meal Cost: "))
TipAmount = float(input("Enter Tip Percent: "))
Tax = 1.11
MealTax = MealCost*Tax
Tiptotal = MealTax*(TipAmount*0.01)
Total = MealTax+Tiptotal
print(round(Total, 2))
