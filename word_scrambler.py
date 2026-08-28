import random
# 50 words for Word Scramble Guessing Game categorized by difficulty

word_list = [
    # --- EASY WORDS (3-4 Letters) ---
    "code", "game", "play", "word", "quiz", 
    "byte", "data", "task", "loop", "file", 
    "math", "team", "luck", "win", "hero",
    
    # --- MEDIUM WORDS (5-6 Letters) ---
    "python", "player", "random", "score", "puzzle", 
    "system", "matrix", "coding", "syntax", "string", 
    "object", "module", "output", "screen", "search", 
    "genius", "vector", "binary", "clever", "winner",
    
    # --- HARD WORDS (7-8 Letters) ---
    "scramble", "guessing", "program", "function", "variable", 
    "compiler", "database", "keyboard", "software", "hardware", 
    "graphics", "terminal", "argument", "sequence", "operator",
    
    # --- EXPERT WORDS (9+ Letters) ---
    "algorithm", "developer", "framework", "interface", "parameter"
]

while True:
    print(' ')
    computer_choice = random.choice(word_list)
    print(''.join(random.sample(computer_choice,len(computer_choice))))
    n = 1
    while n <= 3:
        user_ans = input(f'Enter a correct word (chance {n}): ').lower().strip()
        if not user_ans.isalpha():
            print('Enter only letters!')
            continue
        if not user_ans:
            print('Please enter word!')
            continue
        if user_ans == computer_choice:
            print(' ')
            if n == 1:
                print('Correct word\nYour score is 300')
            elif n == 2:
                print('Correct word\nYour score is 200')
            elif n == 3:
                print('Correct word\nYour score is 100')
            print(' ')
            break
        else:
            if n == 3:
                print(f'\nThe word is {computer_choice}\nYour score is 0\nBetter luck next time!')
            else:
                print('Try again!')
            n += 1
            continue
    if True:
        while True:
            try:
                again_play = int(input("""\nEnter '1' to play again, otherwise '0' : """))
                if again_play not in [0,1]:
                    print("""Value must be '0' or '1' """)
                    continue
            except ValueError:
                print("Enter valid number!")
                continue
            break
        if again_play == 1:
            continue
        else:
            break


            
        
        
