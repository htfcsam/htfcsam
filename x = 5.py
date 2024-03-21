import random

def get_user_choice():
    while True:
        user_choice = input("Please enter Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input! Please enter Rock, Paper, or Scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win! Computer chose " + computer_choice + "."
    else:
        return "You lose! Computer chose " + computer_choice + "."

def play_game():
    user_choice = get_user_choice()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
