class User:
    def __init__(self, income):
        self.income = income


user = User(float(input("Your income:")))
decision = input("Do you wanna rent or sell?(Sell/Rent/Half)")

if decision == "Rent":        
    purchasing_area = float(input("Price of the area in euro:"))
    construction_price = float(input("Price of the construction in euro:"))
    income_after_payments = user.income-construction_price-purchasing_area
    print(income_after_payments)
    construction_maintenance = float(input("Price of the construction maintenance for month in euro:"))
    area = float(input("Enter the area in m*m:"))
    floors = int(input("Enter the number of floors:"))
    construction_area = area*floors
    print(construction_area)
    rent = float(input("Enter the rent price for 1 m*m per month:"))
    income_for_month = (construction_area*rent)-construction_maintenance
    print(income_for_month)
    x = (user.income-income_after_payments)/income_for_month
    print(int(x))

elif decision == "Sell":
    purchasing_area1 = float(input("Price of the area in euro:"))
    construction_price1 = float(input("Price of the construction in euro:"))
    income_after_payments1 = user.income-construction_price-purchasing_area
    selling_area = float(input("Price of the selling area:"))
    gains = selling_area-purchasing_area1-construction_price1
print(gains)
