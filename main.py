class Shoes:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price


shoes = [{"name": "Air Jordan 1", "category": "Sneaker", "description": "BK and WH High Top", "price": 125},
         {"name": "Vans", "category": "Sneaker", "description": "BK and WH Sk8 High Top", "price": 65},
         {"name": "Converse", "category": "Sneaker", "description": "BK and WH Chuck Taylor Low Top", "price": 60},
         {"name": "Becca Flat", "category": "Dress Shoe", "description": "BK Pointed Toe Slingback Flat", "price": 120},
         {"name": "Cole Haan ", "category": "Dress Shoe", "description": "BR Classic Penny Loafer", "price": 158},
         {"name": "Gucci", "category": "Dress Shoe", "description": "BK Leather Lace-Up with Double G", "price": 890},
         {"name": "Birkenstock", "category": "Sandal", "description": "BK Suede Leather", "price": 145},
         {"name": "Crocs", "category": "Sandal", "description": "Hello Kitty Stomp Slide", "price": 50},
         {"name": "Olukai ", "category": "Sandal", "description": "Dark Java Ohana", "price": 75},
         {"name": "Orthofeet", "category": "Indoor Shoe", "description": "BK Louise Stretch Knit", "price": 90},
         {"name": "Diodora", "category": "Indoor Shoe", "description": "WH, OR, and TUR Futsal Boots", "price": 115},
         {"name": "Cloud Slides", "category": "Indoor Shoe", "description": "YL Original", "price": 27}]
subtotal = 20


def payment_type():
    payment = input("Select a payment type: cash, credit, check ")
    while True:
        if payment.lower() == "cash":
            tendered_amount = float(input("Enter amount of cash: "))
            print(f"Your change is {tendered_amount - subtotal}")
            break
        elif payment.lower() == "check":
            check_number = input("Please enter your check number: ")
            while True:
                if len(check_number) < 3 or len(check_number) > 4:
                    check_number = input("Invalid number. Your check number should be 3-4 digits long. Please reenter: ")
                else:
                    break
            break
        elif payment.lower() == "credit":
            credit_card_number = str(input("Please enter your credit card number (no spaces): "))
            while True:
                try:
                    if len(credit_card_number) != 16:
                        credit_card_number = input("Invalid number. Please enter a 16 digit credit card number: ")
                    elif int(credit_card_number) < 0 or int(credit_card_number) > 10 ** 16 - 1:
                        credit_card_number = str(input("Please enter a better number: "))
                    else:
                        print(credit_card_number, "is your credit card number")
                        break
                except ValueError or TypeError:
                    credit_card_number = str(input("Please try again: "))
            expiration = str(input("Please enter your card's expiration date (mmyy): "))
            while True:
                try:
                    if len(expiration) != 4:
                        expiration = str(input("Invalid response. Please enter your card's expiration date in the correct"
                                       " format (mmyy)"))
                    elif int(expiration[0]) > 1 or (int(expiration[2]) != 2 & int(expiration[2]) != 3):
                        expiration = str(input("Invalid response. Please enter again the card's expiration date: "))
                    elif int(expiration[0]) == int(expiration[1]) == 0 or (int(expiration[0]) == 1 and int(expiration[1]) > 2):
                        expiration = str(input("Invalid response. Please enter a valid month: "))
                    elif int(expiration[2]) == 2 and int(expiration[3]) < 4:
                        expiration = str(input("Invalid response. Please enter a valid year: "))
                    else:
                        print(f"{expiration[0:2]}/{expiration[2:4]} is your expiration date")
                        break
                except ValueError or TypeError:
                    expiration = str("Reenter your expiration date: ")
            cvv = str(input("Please enter your card's CVV number: "))
            while True:
                try:
                    if len(cvv) != 3:
                        cvv = input("You must enter a 3-digit number: ")
                    elif int(cvv) < 0 or int(cvv) > 999:
                        cvv = input("Invalid number. Please reenter your cvv number: ")
                    else:
                        print(cvv, "is your cvv number")
                        break
                except ValueError or TypeError:
                    cvv = input("You must enter a 3-digit number: ")
            break
        else:
            payment = input("Invalid response. Please enter: 'cash', 'credit', or 'check'")

            def calculate_totals(subtotal, tax_rate):
                sales_tax = subtotal * tax_rate

                grand_total = subtotal + sales_tax

                subtotal = round(subtotal, 2)
                sales_tax = round(sales_tax, 2)
                grand_total = round(grand_total, 2)

                return subtotal, sales_tax, grand_total

            subtotal = 100.0
            tax_rate = 0.08
            subtotal, sales_tax, grand_total = calculate_totals(subtotal, tax_rate)
            print("Subtotal:", subtotal)
            print("Sales Tax:", sales_tax)
            print("Grand Total:", grand_total)
