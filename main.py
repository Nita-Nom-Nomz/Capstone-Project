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
