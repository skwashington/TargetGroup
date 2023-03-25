def quarter_growth(q1, q2):
    return 100 * ((q2 / q1) - 1)


while True:
    print('Please enter the data concerning Target\'s sale of a product during the first quarter. Dont use the "$" character')
    bought_products = int(input('Q1: How many units of the product did Target buy? (-1 to Quit): '))
    if bought_products == -1:
        break
    buying_price = float(input('Q1: How much did each unit cost Target?: '))
    sold_product = int(input('Q1: How many units of your product did Target sell?: '))
    selling_price = float(input('Q1: How much did Target sell each unit?: '))
    print()

    paid_units = bought_products * buying_price
    sold_units = sold_product * selling_price
    quarterly_profit1 = sold_units - paid_units

    print('Please enter the data concerning Target\'s sale of a product during the second quarter. Dont use the "$" character')
    bought_products2 = int(input('Q2: How many units of the product did Target buy?: '))
    buying_price2 = float(input('Q2: How much did each unit cost Target?: '))
    sold_product2 = int(input('Q2: How many units of your product did Target sell?: '))
    selling_price2 = float(input('Q2: How much did Target sell each unit?: '))
    print()

    paid_units2 = bought_products2 * buying_price2
    sold_units2 = sold_product2 * selling_price2
    quarterly_profit2 = sold_units2 - paid_units2

    growth_percentage = quarter_growth(quarterly_profit1, quarterly_profit2)

    if growth_percentage >= 10:
        print(f'This is a great investment opportunity, the percentage of the products\' growth is {growth_percentage}%')
    elif growth_percentage < 10:
        print(f'This is not a good investment opportunity, the percentage of the products\' growth is {growth_percentage}%')
