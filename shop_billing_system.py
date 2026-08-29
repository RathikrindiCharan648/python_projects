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

def menu():
    return """
    =============== MENU ===============
            1) view products in shop
            2) add to buying cart
            3) customer checkout
            4) finish shopping
        """

def view_list():
    output = ''
    for item, item_details in products.items():
        output += f'{item:<20} : ₹{item_details['price']:,.2f}\n'
    return output
    
def add_cart():
    while True:
            item_name = input("\nEnter product name : ").strip().lower()
            if not item_name.replace(' ','').isalpha():
                print('Invalid product name! Try again')
                continue
            elif item_name not in products:
                print("This product is not there in this shop!")
                continue
            else:
                break

    if products[item_name]['stock'] == 0:
        return f"\nOut of stock! No stock is available for {item_name}!"

    while True:
        try:
            total_items = int(input("Enter how many products you want : "))
            if total_items < 1:
                print('Invalid number! Try again.')
                continue
            elif total_items > products[item_name]['stock']:
                print(f"\nInsufficient stock! only {products[item_name]['stock']} is there!")
                continue
            else:
                products[item_name]['stock'] -= total_items
                if item_name in shopping_cart:
                    shopping_cart[item_name] += total_items
                else:
                    shopping_cart[item_name] = total_items
                return f"\n{total_items} {item_name} added to cart successfully!"
        except ValueError:
            print("Enter only numbers!")
            continue
    
def billing():
    if not shopping_cart:
        print("Shopping cart is empty!")
        return 
    else:
        amount_list = []
        for item, stocks in shopping_cart.items():
            total_amount = products[item]['price'] * stocks
            amount_list.append(total_amount)
    if amount_list:
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

def exit_shop():
    return "================= Finish shopping =================\n"

def choose_menu():
    while True:
        try:
            selection = int(input('\nEnter your choice(from menu) : '))
            print(' ')
            if selection < 1 or selection > 4:
                print('\nChoose in range (1 - 4) only!')
                continue
        except ValueError:
            print('Invalid choose! Try again')
            continue
        break
    return selection

if __name__ == '__main__':
    while True:
        print(menu())
        user_selection = choose_menu()
        if user_selection == 1:
            print(view_list())
        elif user_selection == 2:
            print(add_cart())
        elif user_selection == 3:
            billing()
        else:
            print(exit_shop())
            break
