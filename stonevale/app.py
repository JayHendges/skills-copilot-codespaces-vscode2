import random

# Initialize scores for both warriors
rok_score = 0
paprya_score = 0

# Define the moves for each warrior
rok_moves = ["scissors", "paper", "scissors", "rock", "rock"]
paprya_moves = ["rock", "rock", "paper", "scissors", "paper"]

# Function to validate the move
def validate_move(move):
    valid_moves = ["rock", "paper", "scissors"]
    while move not in valid_moves:
        random_move = random.choice(valid_moves)
        print(f"Invalid move! Please enter 'rock', 'paper', or 'scissors'. Hint: You can try '{random_move}'.")
        move = input("Enter your move: ")
    return move

# Simulate the duel for 5 rounds
for round_num in range(5):
    random_move = random.choice(["rock", "paper", "scissors"])
    print(f"Please enter 'rock', 'paper', or 'scissors'. Hint: You can try '{random_move}'.")
    rok_move = input("Enter Rok's move: ")
    rok_move = validate_move(rok_move)

    paprya_move = random.choice(["rock", "paper", "scissors"])
    print(f"Paprya's move: {paprya_move}")

    # Determine the winner of the round and award points
    if rok_move == paprya_move:
        print(f"Round {round_num+1}: Draw")
        rok_score += 0
        paprya_score += 0
    elif (rok_move == "rock" and paprya_move == "scissors") or (rok_move == "paper" and paprya_move == "rock") or (rok_move == "scissors" and paprya_move == "paper"):
        if rok_move == "rock":
            rok_score += 1
        elif rok_move == "paper":
            rok_score += 2
        else:
            rok_score += 3
        print(f"Round {round_num+1}: Rok wins")
    else:
        if paprya_move == "rock":
            paprya_score += 1
        elif paprya_move == "paper":
            paprya_score += 2
        else:
            paprya_score += 3
        print(f"Round {round_num+1}: Paprya wins")

# Tally the scores
print(f"\nFinal Scores:\nRok: {rok_score} points\nPaprya: {paprya_score} points")

# Declare the overall winner of the duel
if rok_score > paprya_score:
    print("Rok wins the duel!")
elif rok_score < paprya_score:
    print("Paprya wins the duel!")
else:
    print("The duel ends in a tie!")
