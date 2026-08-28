# Expence Tracker 

# empty dictionary for categories and amount 
categories_dict = {}

# Menu list 

print("""
    ====================== MENU LIST ======================\n
    1) Add expense
    2) View Total Spending
    3) view spending by category
    4) EXIT
    """)

while True:

# Error handiling

    try:
        user_selection = int(input('\nEnter your choose number from menu : '))
        print(' ')
        if user_selection <= 0 or user_selection > 4:
            print('Please enter the number from 1 - 4\n')
            continue
    except ValueError:
        print('Invalid choose! Try again.\n')
        continue

# check the choose 

    if user_selection == 1:
        try:
            expense_amount = float(int(input('Enter your expense Amount : ')))
            if expense_amount < 0:
                print("Enter valid amount!\n")
                continue
        except ValueError:
            print("Invalid AMOUNT! Try again.\n") 
            continue

        try:
            category = input("Enter category(e.g., Food, Transport, Clothes) : ").strip().capitalize()
            if not category.replace(' ','').isalpha():
                print("Invalid caregory! Try again.")
                continue
            if category in categories_dict:
                categories_dict[category] += expense_amount
            else:
                categories_dict[category] = expense_amount
            print(f"Expense of ${expense_amount} added under {category} category!\n")
        except ValueError:
            print("Enter valid category!")
            continue

    elif user_selection == 2:
        print(f"Wait a second calculating...")  
        if categories_dict:
            print(f'Total spending : ${sum(categories_dict.values()):,.2F}')
        else:
            print("Please add expenses...")
            continue

    elif user_selection == 3:
        if not categories_dict:
            print("Category list is empty.")
            continue
        for key, value in categories_dict.items():
            print(f"{key} : {value}")

    else:
        print("Exiting program! Thanks for using Expense Tracker")
        break





