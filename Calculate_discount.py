def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount =price *(discount_percent/100)
        correct_answer = price - discount 
        return correct_answer
    else:
        return price
user_price = float(input("Enter the price?"))
user_discount = float(input("Enter the dicount in percentage form:"))
result = calculate_discount(user_price,user_discount)
print(result)
