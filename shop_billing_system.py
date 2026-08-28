# Retail electronics shop

products = {
    'wireless mouse'    : {'price' : 699.00, 'stock' : 10},
    'wireless keyboard' : {'price' : 1499.00, 'stock' : 10},
    'head phones'       : {'price' : 499.00, 'stock' : 19},
    'power bank'        : {'price' : 1499.00, 'stock' : 30},
    'laptop'            : {'price' : 74999.00, 'stock' : 5},
    'smart watch'       : {'price' : 1999.00, 'stock' : 34},
    'bluetooth speaker' : {'price' : 14999.00, 'stock' : 14},
    'doccument scanner' : {'price' : 25999.00, 'stock' : 7},
    'mobile phone'      : {'price' : 28999.00, 'stock' : 15},
    'smart televison'   : {'price' : 105999.00, 'stock' : 6},
    'desktop'           : {'price' : 185999.00, 'stock' : 8}
}

shopping_cart = {}

print("""
        =============== MENU ===============
        1) view products in shop
        2) add to cart
        3) customer checkout
        4) finish shopping
    """)
while True:
    try:
        user_selection = int(input('\nEnter your choice(from menu) : '))
        if user_selection < 1 or user_selection > 4:
            print('\nChoose in range (1 - 4) only!')
            continue
    except ValueError:
        print('Invalid choose! Try again')
        continue

    if user_selection == 1:
        print('\nThis is products list in shop')
        print('  ')
        for key, value in products.items():
            print(f'  {key}  -   {value['price']}')
        continue

    elif user_selection == 2:
        while True:
            item_name = input("\nEnter product name : ").strip().lower()
            if not item_name.replace(' ','').isalpha():
                print('Invalid product name! Try again')
                continue
            elif item_name not in products:
                print("This product is not there in this shop!")
                continue
            else:
                if item_name in products:
                    while True:
                        try:
                            total_items = int(input("Enter how many products you want : "))
                            if total_items < 1:
                                print('Invalid number! Try again.')
                                continue
                            elif products[item_name]['stock'] == 0:
                                print(f"\nInsufficient funds! No stock is available!")
                                break
                            elif total_items > products[item_name]['stock']:
                                print(f"\nInsufficient funds! only {products[item_name]['stock']} is there!")
                                continue
                            else:
                                products[item_name]['stock'] = products[item_name]['stock'] - total_items
                                if item_name in shopping_cart:
                                    shopping_cart[item_name] += total_items
                                else:
                                    shopping_cart[item_name] = total_items
                                break
                        except ValueError:
                            print("Enter only numbers!")
                            continue
                    break
    elif user_selection == 3:
        if not shopping_cart:
            print("Shopping cart is empty!")
            continue
        elif shopping_cart:
            amount_list = []
            for item, stocks in shopping_cart.items():
                total_amount = products[item]['price'] * stocks
                amount_list.append(total_amount)
        if total_amount:
            print(' ')
            print(f'''
------------------------------- Shopping Reciept ----------------------------------
            ''')
            for key, value in shopping_cart.items():
                print(f'{key.capitalize()} * {value}  = {(products[key]['price']*value):,.2F}')
            print(f'\n---------Grand Total --> {sum(amount_list):,.2F}---------')
            print('\n =========================== THANKS FOR SHOPPING =============================')  
            amount_list.clear()
            shopping_cart.clear()
    else:
        print("================= Finish shopping =================\n")
        break