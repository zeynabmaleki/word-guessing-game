import random

print("Welcome to the Game!")

user_input = input("Do you want to play? (y/n) ").lower()

# words = ['rainbow', 'computer', 'science', 'programming',
#          'python', 'mathematics', 'player', 'condition',
#          'reverse', 'water', 'board', 'geeks']
words = ['bee', 'pee']
word = random.choice(words)

if user_input == 'y':
    turns = 5
    user_guess = ''

    while turns > 0:
        guess = 1
        failed = 0
        
        for char in word:
            if char in user_guess:
                print(char, end=" ")

            else:
                print("_")
                failed += 1

            if failed == 0:
                print("You Win")
                print("The word is: ", word)
                break

        print()
        guess = input("guess a character:")
        user_guess += guess

        if guess not in word:
            turns -= 1
            print(f'wrong! you have {turns} turns.')
            if turns == 0:
                print("Game over!")


else:
    print("Bye!")