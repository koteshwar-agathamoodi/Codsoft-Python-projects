import random
options = {
    "R":"rock",
    "S":"scissors",
    "P":"paper"
}
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
        

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() in ["yes","y"]

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock(R), paper(P), or scissors(S): ")
        computer_choice = random.choice(list(options.values()))
        user_choice = user_choice.upper()

        if user_choice not in options:
            print("Please select valid options from "+",".join(list(options.keys())))
            continue
        
        user_choice = options[user_choice]

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print("Your score:", user_score)
        print("Computer's score:", computer_score)

        if not play_again():
            break

rock_paper_scissors()
