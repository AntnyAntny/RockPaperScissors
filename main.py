import random
choices = ["rock", "paper", "scissors"]
playerChoice = None
computerChoice = random.choice(choices)

while playerChoice not in choices:
    playerChoice = input("Rock, Paper, or Scissors? ").lower()

print(f"You chose {playerChoice}.")
print(f"The computer chose {computerChoice}.")

if playerChoice == computerChoice:
    print("Draw!")
elif playerChoice == "rock" and computerChoice == "scissors":
    print("You win!")
elif playerChoice == "paper" and computerChoice == "rock":
    print("You win!")
elif playerChoice == "scissors" and computerChoice == "paper":
    print("You win!")
else:
    print("Rip bozo")

