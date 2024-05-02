import random

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(valid_choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    elif (user_choice == 'rock' and computer_choice == 'paper') or \
         (user_choice == 'scissors' and computer_choice == 'rock') or \
         (user_choice == 'paper' and computer_choice == 'scissors'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
