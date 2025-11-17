import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'exit' to quit the game.\n")

player_score = 0
computer_score = 0

while True:
    player = input("Choose (rock/paper/scissors): ").lower()

    if player == "exit":
        print("\nThanks for playing!")
        print(f"Final Score → You: {player_score} | Computer: {computer_score}")
        break

    if player not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice, try again!")
        continue

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    result = get_winner(player, computer)
    if result == "player":
        player_score += 1
        print("✅ You win this round!")
    elif result == "computer":
        computer_score += 1
        print("❌ Computer wins this round!")
    else:
        print("🤝 It's a draw!")

    print(f"Score → You: {player_score} | Computer: {computer_score}\n")