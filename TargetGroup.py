#CALCULATES SALES FROM MONTH TO MONTH

# Initialize a list to store the sales data for each product in the  month
sales_data = {}
print('Type "stop" to stop')
while True:
    print("For this month, enter product and its average sale")
    product_name = input("Product name: ")
    if product_name == "stop":
        continue
    product_inventory = float(input("Units bought: "))
    unit_price = float(input("Price of one unit: $"))
    sales_prompt = float(input("Enter average sales: $"))

    # Add the sales data to the sales_data dictionary
    if product_name not in sales_data:
        sales_data[product_name] = sales_prompt
    else:
        sales_data[product_name] += sales_prompt


    units_sold = sales_prompt // unit_price
    profit_percentage = ((unit_price - (unit_price / 2)) / unit_price) * 100
    if units_sold >= 150:
        print()
        print(f"Monthly profit percentage: {profit_percentage:.2f}%")
        print('Profit of at least 150% made, reorder')
    elif units_sold == 100:
        print()
        print(f"Monthly profit percentage: {profit_percentage:.2f}%")
        print('Profit is equal to money invested for inventory, order less inventory')
    elif units_sold < 100:
        print()
        print(f"Monthly profit percentage: {profit_percentage:.2f}%")
        print('Profit not made back, consider not reordering ')





