class Bank:
    def __init__(self,name,mobile_number):
        self.name = name
        self.mobile_number = mobile_number
        self.balence = 0.0

    def deposite(self,amount):
        self.balence += amount
        return f"Mr/Mrs {self.name},you deposite ₹ {amount:,.2F}.\nMessage will be sent to your mobile number ******{str(self.mobile_number)[6:]}. -> Bank Balence ₹ {self.balence:,.2f}"
    
    def withdrawl(self,amount):
        self.balence -= amount
        if self.balence < 0.0:
            self.balence += amount
            return f"Insufficient Funds\nyour current balence is ₹ {self.balence:,.2f}"
        return f"Mr/Mrs {self.name},you withdrawl ₹ {amount:,.2F}.\nMessage will be sent to your mobile number ******{str(self.mobile_number)[6:]}. -> Bank Balence ₹ {self.balence:,.2f}"
    
while True:
    user_name = input("Enter your Name : ").strip()
    if not user_name or not user_name.replace(" ","").isalpha():
        print("Invalid Name!")
        continue
    break

while True:
    try:
        user_number = int(input("Enter your mobile number : "))
        if not user_number or not len(str(user_number)) == 10 or not user_number >= 6001000000:
            print("Invalid Mobile Number!")
            continue
        break
    except ValueError:
        print("Invalid Mobile Number!")

my_class = Bank(user_name,user_number)

while True:
    print("\n1) Deposite\n2) Withdrawl")
    while True:
        try:
            choose = int(input("Enter your choose : "))
            if choose != 1 and choose != 2:
                print("Choose only 1 or 2!")
                continue
            break
        except ValueError:
            print("Invalid value!")

    if choose == 1:
        while True:
            try:
                deposit_money = int(input("\nDEPOSITE MONEY : "))
                if not deposit_money or deposit_money < 0:
                    print("Invalid Amount!")
                    continue
                break
            except ValueError:
                print("Invalid Amount!")
        print(my_class.deposite(deposit_money))
            
    if choose == 2:
        while True:
            try:
                withdrawl_money = int(input("\nWITHDRAWL MONEY : "))
                if not withdrawl_money or withdrawl_money < 0:
                    print("Invalid Amount!")
                    continue
                break
            except ValueError:
                print("Invalid Amount!")
        print(my_class.withdrawl(withdrawl_money))
    while True:
        exit = input("""\nEnter 'e' to FINISH otherwise 'p' to proceed : """).strip().lower()
        if not exit:
            print('''Enter 'e' Or 'p' To Continue...''')
            continue
        elif not exit == 'e' and not exit == 'p':
            print('''Enter only 'e' or 'p' ''')
            continue
        break
    if exit == 'e':
        break
    elif exit == 'p':
        continue
