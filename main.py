# Shenedia code start ===============================================================================================
class Shoe:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price


shoes = [Shoe("Air Jordan 1", "Sneaker", "BK and WH High Top", 125),
         Shoe("Vans", "Sneaker", "BK and WH Sk8 High Top", 65),
         Shoe("Converse", "Sneaker", "BK and WH Chuck Taylor Low Top", 60),
         Shoe("Becca Flat", "Dress Shoe", "BK Pointed Toe Slingback Flat", 120),
         Shoe("Cole Haan", "Dress Shoe", "BR Classic Penny Loafer", 158),
         Shoe("Gucci", "Dress Shoe", "BK Leather Lace-Up with Double G", 890),
         Shoe("Birkenstock", "Sandal", "BK Suede Leather", 145),
         Shoe("Crocs", "Sandal", "Hello Kitty Stomp Slide", 50),
         Shoe("Olukai1", "Sandal", "Dark Java Ohana", 75),
         Shoe("Orthofeet", "Indoor Shoe", "BK Louise Stretch Knit", 90),
         Shoe("Diodora", "Indoor Shoe", "WH, OR, and TUR Futsal Boots", 115),
         Shoe("Cloud Slides", "Indoor Shoe", "YL Original", 27)]

total_items = []  # will hold selected items from menu in this list


# what was added for menu selection start
def display_menu(shoes):
    for select, shoe in enumerate(shoes, 1):
        print(f"{select}. {shoe.name} - {shoe.category} - {shoe.description} - ${shoe.price}")


display_menu(shoes)


def take_order(shoes):
    while True:
        items = input("Please select the item by number you wish to purchase or type 'done' when finished.\n>")
        if items.lower == 'done':
            break
        else:
            try:
                item_number = int(items)
                if 1 <= item_number <= len(shoes):
                    total_items.append(shoes[item_number - 1])
                    print(f"{shoes[item_number - 1].name} added to cart.")
                else:
                    print("Invalid item number. Please select a valid item.")
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")


take_order(shoes)
#  what was added for menu selection end
# Shenedia code end=============================================================================================

# Jay's Code start ====================================================================================================
subtotal = 20


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

# Jay's Code end ====================================================================================================


# Clay's Code start =================================================================================================
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
# Clay's Code end =================================================================================================


"""
Redid the code with a class base
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
        if payment_type == 'cash':
            amount_tendered = float(input("Enter amount tendered: $"))
            change = amount_tendered - grand_total
            print(f"Change: ${change:.2f}")
        elif payment_type == 'credit':
            card_number = input("Enter credit card number: ")
            expiration_date = input("Enter expiration date (MM/YY): ")
            cvv = input("Enter CVV: ")
            print("Payment successful with credit card.")
        elif payment_type == 'check':
            check_number = input("Enter check number: ")
            print("Payment successful with check.")
        else:
            print("Invalid payment type.")

        self.cart = []

    def start(self):
        while True:
            self.display_menu()
            choice = input("\nEnter item number to add to cart or 'checkout' to complete the purchase: ")
            if choice.lower() == 'checkout':
                tax_rate = 0.08  # Example tax rate
                self.checkout(tax_rate)
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
"""
