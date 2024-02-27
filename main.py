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
            break
        elif payment.lower() == "credit":
            credit_card_number = input("Please enter your credit card number: ")
            expiration = input("Please enter your card's expiration date (mm/yy): ")
            cvv = input("Please enter your card's CVV number: ")
            break
        else:
            payment = input("Invalid response. Please enter: 'cash', 'credit', or 'check'")
