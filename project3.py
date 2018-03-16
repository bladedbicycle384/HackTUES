from tkinter import *
	
def Decision(decision):
	if decision == "Rent":
		w = Label(root, Rent(decision))
		w.pack()
	elif decision == "Sell":
		w = Label(root, Sell(decision))
		w.pack()
	elif decision == "Chance":
		w = Label(root, Chance(decision))
		w.pack()
				
def Rent():      
    purchasing_area = float(input("Price of the area in euro:"))
    complextruction_price = float(input("Price of the construction in euro:"))
    area = float(input("Enter the area in m*m:"))
    floors = int(input("Enter the number of floors:"))
    construction_area = area*floors
    rent = float(input("Enter the rent price for 1 m*m per month:"))
    income_for_month = (construction_area*rent)-construction_maintenance
    x = (user.income-residue_after_payments)/income_for_month
    construction_maintenance = float(input("Price of the construction maintenance for month in euro:"))
    residue_after_payments = user.income-construction_price-purchasing_area
    if residue_after_payments >= 0:
        w = Label(root,residue_after_payments, text = "There are")
        w.pack()
        w = Label(root, text = "euros left!")
        w.pack()
	
    else:
        q = Label("You must pay", 0-residue_after_payments, "euro!")
        q.pack()
        e = Label(root,int(x), text = "You can make the payment after:")
        e.pack()
        r = Label(root,income_for_month, text = 'Income for month is')
        r.pack()
        t = Label(root,construction_area, text = "The summarized area is")
        t.pack()

def Sell():
    purchasing_area1 = float(input("Price of the area in euro:"))
    construction_price1 = float(input("Price of the construction in euro:"))
    income_after_payments1 = user.income-construction_price-purchasing_area
    selling_area = float(input("Price of the selling area:"))
    gains = selling_area-purchasing_area1-construction_price1
    y = Label("Your gains are", gains)
    y.pack()

def Chance():
    percentage_of_sellings = float(input("The percentage of the sellings(The part of your possessions you want to sell.):"))
    percentage_of_rents = float(input("The percentage of the rents(The part of things(for example: apartments)you want to rent.):"))
    construction_price1 = float(input("Price of the construction in euro:"))
    purchasing_area1 = float(input("Price of the area in euro:"))
    selling_area = float(input("Price of the selling area:"))
    residue_after_payments = user.income-construction_price1-purchasing_area1
    gains = selling_area-purchasing_area1-construction_price1
    earnings = (percentage_of_rents/100)*residue_after_payments - (percentage_of_sellings/100)*gains
	
    if earnings > 0:
        u = Label(root, earnings, text = "You will receive")
        u.pack()
        o = Label(root, text = "Do it if you want!")
        o.pack()
        
    elif earnings == 0:
        p = Label(root, text = "You will not receive anything!")
        p.pack()
        a = Label(root, text = "There is no point of doing this!")
        a.pack()
	
    else:
        s = Label(root, text = "You must pay")
        s.pack()
        s = Label(root, 0 - earnings, text = "euro!")
        d = Label(root, text = "Do NOT do this!")
        d.pack()
		
class User:
    def __init__(self, income):
        self.income = income

user = User(float(input("Your income:")))
decision = str(input("What do you want to do?(Sell/Rent/Chance)"))
