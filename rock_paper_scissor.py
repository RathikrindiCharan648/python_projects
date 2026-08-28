import random

print("Choose your option")
print(['rock', 'paper', 'scissor'])

user_score_list = []
computer_score_list = []

while True:
    option_list = ['rock', 'paper', 'scissor']
    computer_choose = random.choice(option_list)
    user_selection = input('\nSelect your choose : ').lower().strip()
    
    if not user_selection:
        print('please enter your choose!')
        continue
    if not user_selection.isalpha():
        print('Invalid choose!')
        continue
    if user_selection != 'rock' and user_selection != 'paper' and user_selection != 'scissor':
        print('Enter only one of the item in list!')
        continue
        
    if computer_choose == user_selection:
        print(f'Computer chooses {computer_choose}')  # Added here so TIE rounds reveal choice too!
        print('0 points to each other,TIE...')
        continue
        
    print(f'Computer chooses {computer_choose}')
    
    if computer_choose == 'rock':
        if user_selection == "paper":
            user_score_list.append(1)
            if sum(user_score_list) == 3:
                print('User is final winner!')
                break
            print(f'Your score is {sum(user_score_list)}')
        if user_selection == "scissor":
            computer_score_list.append(1)
            if sum(computer_score_list) == 3:
                print('Final winner is computer!')
                break
            print(f'Computer score is {sum(computer_score_list)}')
        continue

    if computer_choose == 'paper':
        if user_selection == "scissor":
            user_score_list.append(1)
            if sum(user_score_list) == 3:
                print('User is final winner!')
                break
            print(f'Your score is {sum(user_score_list)}')
        if user_selection == "rock":
            computer_score_list.append(1)
            if sum(computer_score_list) == 3:
                print('Final winner is computer!')
                break
            print(f'Computer score is {sum(computer_score_list)}')
        continue

    if computer_choose == 'scissor':
        if user_selection == "rock":
            user_score_list.append(1)
            if sum(user_score_list) == 3:
                print('Congratulations You win this GAME!')
                break
            print(f'Your score is {sum(user_score_list)}')
        if user_selection == "paper":
            computer_score_list.append(1)
            if sum(computer_score_list) == 3:
                print('Computer win this game!')
                break
            print(f'Computer score is {sum(computer_score_list)}')
        continue
