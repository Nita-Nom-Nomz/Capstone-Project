

class Product:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.category} - {self.description} - ${self.price:.2f}"


class CashRegister:
    def __init__(self):
        self.products = [Product(**shoe) for shoe in shoes]
        self.cart = []

    def display_menu(self):
        print("Welcome to the Self-Service Terminal!")
        print("Menu:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")

    def add_to_cart(self, item_number, quantity):
        product = self.products[item_number - 1]
        self.cart.append((product, quantity))
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def calculate_totals(self, tax_rate):
        subtotal = sum(product.price * quantity for product, quantity in self.cart)
        sales_tax = subtotal * tax_rate
        grand_total = subtotal + sales_tax
        return subtotal, sales_tax, grand_total

    def checkout(self, tax_rate):
        subtotal, sales_tax, grand_total = self.calculate_totals(tax_rate)
        print("\nReceipt:")
        print("Items:")
        for product, quantity in self.cart:
            print(f"{product.name}: {quantity} x ${product.price:.2f} = ${product.price * quantity:.2f}")
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Grand Total: ${grand_total:.2f}")
        payment_type = input("\nChoose payment type - (cash / credit / check): ").lower()
        while True:
            if payment_type.lower() == 'cash':
                amount_tendered = str(input("Enter amount tendered: $"))
                while True:
                    try:
                        if float(amount_tendered) >= grand_total:
                            change = float(amount_tendered) - grand_total
                            print(f"Your change is ${round(change, 2)}")
                            return
                        else:
                            amount_tendered = float(input("Please enter a sufficient amount of cash: "))
                    except ValueError or TypeError:
                        amount_tendered = input("Enter valid amount tendered: $")
                        continue
            elif payment_type.lower() == 'credit':
                card_number = input("Enter credit card number: ")
                while True:
                    try:
                        if len(card_number) != 16:
                            card_number = input("Invalid number. Please enter a 16 digit credit card number: ")
                        elif int(card_number) < 0 or int(card_number) > 10 ** 16 - 1:
                            card_number = str(input("Please enter a better number: "))
                        else:
                            print(card_number, "is your credit card number")
                            break
                    except ValueError or TypeError:
                        card_number = str(input("Please try again: "))
                        continue
                expiration_date = input("Enter expiration date (MMYY): ")
                while True:
                    try:
                        if len(expiration_date) != 4:
                            expiration_date = str(
                                input("Invalid response. Please enter your card's expiration date in the correct"
                                      " format (MMYY)"))
                        elif int(expiration_date[0]) > 1 or int(expiration_date[2]) < 2 or int(expiration_date[2]) > 3:
                            expiration_date = str(
                                input("Invalid response. Please enter again the card's expiration date: "))
                        elif int(expiration_date[0]) == int(expiration_date[1]) == 0 or (
                                int(expiration_date[0]) == 1 and int(expiration_date[1]) > 2):
                            expiration_date = str(input("Invalid response. Please enter a valid month: "))
                        elif int(expiration_date[2]) == 2 and int(expiration_date[3]) < 4:
                            expiration_date = str(input("Invalid response. Please enter a valid year: "))
                        else:
                            print(f"{expiration_date[0:2]}/{expiration_date[2:4]} is your expiration date")
                            break
                    except ValueError or TypeError:
                        expiration_date = str("Reenter your expiration date: ")
                        continue
                cvv = input("Enter CVV: ")
                while True:
                    try:
                        if len(cvv) != 3:
                            cvv = input("You must enter a 3-digit number: ")
                        elif int(cvv) < 0 or int(cvv) > 999:
                            cvv = input("Invalid number. Please reenter your CVV number: ")
                        else:
                            print(cvv, "is your CVV number")
                            print("Payment successful with credit card.")
                            print(f"Card number: {card_number}\nExpiration date: {expiration_date[0:2]}"
                                  f"/{expiration_date[2:4]}\nCVV: {cvv} ")
                            return
                    except ValueError or TypeError:
                        cvv = input("You must enter a 3-digit number: ")
                        continue
            elif payment_type.lower() == 'check':
                check_number = input("Enter check number: ")
                while True:
                    try:
                        if len(check_number) < 3 or len(check_number) > 4:
                            check_number = input("Invalid number. Please reenter a 3-4 digit long number: ")
                        elif int(check_number) <= 0 or int(check_number) > 9999:
                            check_number = input("Invalid value. Please reenter: ")
                        else:
                            print(f"Your check number is {check_number}.")
                            return
                    except ValueError or TypeError:
                        check_number = input("Please reenter 3-4 numbers: ")
                        continue
            else:
                print("Invalid payment type.")
                payment_type = input("\nChoose payment type - (cash / credit / check): ").lower()
            self.cart = []

    def start(self):
        while True:
            self.display_menu()
            choice = input("\nEnter item number to add to cart or 'checkout' to complete the purchase: ")
            if choice.lower() == 'checkout':
                tax_rate = 0.08  # Example tax rate
                self.checkout(tax_rate)
                break
            else:
                try:
                    item_number = int(choice)
                    if 1 <= item_number <= len(self.products):
                        quantity = int(input("Enter quantity: "))
                        self.add_to_cart(item_number, quantity)

                    else:
                        print("Invalid item number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid item number or 'checkout'.")


# List of products
shoes = [
    {"name": "Air Jordan 1", "category": "Sneaker", "description": "BK and WH High Top", "price": 125},
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
    {"name": "Cloud Slides", "category": "Indoor Shoe", "description": "YL Original", "price": 27}
]
register = CashRegister()
register.start()
