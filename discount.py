# creating a function to calculate discount
def calculate_discount(price, discount_percentage):

    if discount_percentage >= 20:
       discount_amount = (discount_percentage / 100) * price
       return discount_amount
    else:
        return ('no discount was given your price is:',price)
    
    # prompting the user for input
price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

print(f"The discount amount is: {calculate_discount(price, discount_percentage)}")