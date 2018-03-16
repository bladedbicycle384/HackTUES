class User:
    def __init__(self, income):
        self.income = income

user = User(float(input("Your income:")))
decision = input("What do you want to do?(Sell/Rent/Chance)")

if decision == "Rent":        
    purchasing_area = float(input("Price of the area in euro:"))
    construction_price = float(input("Price of the construction in euro:"))
    area = float(input("Enter the area in m*m:"))
    floors = int(input("Enter the number of floors:"))
    construction_area = area*floors
    rent = float(input("Enter the rent price for 1 m*m per month:"))
    income_for_month = (construction_area*rent)-construction_maintenance
    x = (user.income-residue_after_payments)/income_for_month
    construction_maintenance = float(input("Price of the construction maintenance for month in euro:"))
    residue_after_payments = user.income-construction_price-purchasing_area
    if residue_after_payments >= 0:    
        print("There are", residue_after_payments, "euros left!")
		
    else:
        print("You must pay", 0-residue_after_payments, "euro!")

    print("You can make the payment after:", int(x))
    print('Income for month is', income_for_month)
    print("The summarized area is", construction_area)
	
elif decision == "Sell":
    purchasing_area1 = float(input("Price of the area in euro:"))
    construction_price1 = float(input("Price of the construction in euro:"))
    income_after_payments1 = user.income-construction_price-purchasing_area
    selling_area = float(input("Price of the selling area:"))
    gains = selling_area-purchasing_area1-construction_price1
    print("Your gains are", gains)

else:
    percentage_of_sellings = float(input("The percentage of the sellings(The part of your possessions you want to sell.):"))
    percentage_of_rents = float(input("The percentage of the rents(The part of things(for example: apartments)you want to rent.):"))
    construction_price = float(input("Price of the construction in euro:"))
    purchasing_area1 = float(input("Price of the area in euro:"))
    purchasing_area = float(input("Price of the area in euro:"))
    selling_area = float(input("Price of the selling area:"))
    construction_price1 = float(input("Price of the construction in euro:"))
    residue_after_payments = user.income-construction_price-purchasing_area
    gains = selling_area-purchasing_area1-construction_price1
    earnings = (percentage_of_sellings/100)*gains - (percentage_of_rents/100)*residue_after_payments	
	
if earnings > 0:
    print(earnings)
    print("Do it if you want!")

elif earnings == 0:
	print(earnings)
	print("There is no point of doing this!")
	
else:
	print("You must pay", 0 - earnings, "euro!")
	print("Do NOT do this!")

