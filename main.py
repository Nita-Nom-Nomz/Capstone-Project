subtotal = 20
def payment_type():
    payment = input("Select a payment type: cash, credit, check ")
    while True:
        if payment == "cash":
            tendered_amount = float(input("Enter amount of cash: "))
            print(f"Your change is {tendered_amount - subtotal}")
            break
        elif payment == "check":
            check_number = input("Please enter your check number: ")
            break
        elif payment == "credit":
            credit_card_number = input("Please enter your credit card number: ")
            expiration = input("Please enter your card's expiration date (mm/yy): ")
            CVV = input("Please enter your card's CVV number: ")
            break
        else:
            payment = input("Invalid response. Please enter: 'cash', 'credit', or 'check'")
