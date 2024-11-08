import random

moves = ["rock", "paper", "scissors"]
game_points = []
user_points = 0
computer_points = 0


def computer_move():
    """
    Here we randomised the computer moves
    """
    return random.choice(moves)


def player_move():
    """
    We let the player choice what to do
    """
    choice = input("Please write your move: (rock/paper/scissors): ").lower().strip()
    if choice not in moves:
        print("Invalid input, try again")
        return None
    return choice


def winner(comp_choice, user_choice):
    """
    With the function of winner, we choose how it works if the user choice one thing
    and the computer other
    """
    if user_choice == comp_choice:
        return "Its a tie"
    elif (
        (user_choice == "rock" and comp_choice == "scissors")
        or (user_choice == "paper" and comp_choice == "rock")
        or (user_choice == "scissors" and comp_choice == "paper")
    ):
        return "Player won"
    else:
        return "Computer won"


while True:
    computer_choice = computer_move()
    player_choice = player_move()

    if player_choice is None:
        continue

    result = winner(computer_choice, player_choice)
    game_points.append(result)

    print(f"Player choice: {player_choice}")
    print(f"Machine choice: {computer_choice}")
    print(f"\nResult: {result}")

    if result == "Player won":
        user_points += 1

    if result == "Computer won":
        computer_points += 1

    play_again = input("Do you want to play again?: (yes/no)").strip().lower()
    if play_again != "yes":
        print("\nGame over, thanks for playing")
        break

print(f"\nGame summary: {game_points}")
for index, result in enumerate(game_points):
    print(f"[{index}], {result} ")

print(f"Player wins: {user_points}")
print(f"Computer wins: {computer_points}")
