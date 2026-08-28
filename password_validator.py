class Password_validator:
    def __init__(self,password):
        self.password = password
        self.score = 0

    def valid_check(self):
        self.score = 0
        if self.password.strip() == '':
            return """Password can't be empty"""
        if len(self.password) >= 8:
            self.score += 1
        if any(i.islower() for i in self.password):
            self.score += 1
        if any(i.isupper() for i in self.password):
            self.score += 1
        if any(i.isdigit() for i in self.password):
            self.score += 1
        for i in self.password:
            if i in '!@#$%^&*()_+;:,.<>|-/':
                self.score += 1
                break
        return f"your password score is {self.score}"
                

    def password_status(self):
        if self.score <= 1:
            return 'Very weak! Add mixed charecter and numbers immediately.'
        elif self.score == 2:
            return 'Fair ! Use uppercase, lowercase letters, numbers and charecters.'
        elif self.score == 3 or self.score == 4:
            if not any(i.isdigit() for i in self.password):
                return 'Strong! Great combination of criteria.Use numbers for full secure!'
            elif not len(self.password) >= 8:
                return 'Strong! Great combination of criteria.Use long password is good!'
            return 'Strong! Great combination of criteria.'
        else:
            return "Excellent! Maximum security is achevied."

while True:
    user_password = input('Enter your password : ')
    if not user_password:
        print('Please enter Password!')
        continue
    break

my_class = Password_validator(user_password)
print(my_class.valid_check())
print(my_class.password_status())