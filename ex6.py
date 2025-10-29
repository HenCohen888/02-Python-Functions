#the function Gets a price.
#If price > 1000: ask for custom discount percent from the user.
# Otherwise: apply automatic 10% discount.
# Return the discounted price.

def final_price (price):

    if price > 1000:
        precent = float(input("please enter the discount precent:"))
        discount_value = (100 - precent) / 100
        new_price = price * discount_value
        return new_price
    else:
        new_price = price * 0.9
        return new_price

x = float(input("please enter the product price:"))
result = final_price(x)
print("the price after discount is: ", result)

