
import random


def play_game():
    chips = 2000
    cumulative_bets = 0
    target = 10000

    while chips > 0 and cumulative_bets < target:
        bet = 1  # Strategy: always bet 1 chip

        cumulative_bets += bet

        if random.random() < 0.40:
            chips += bet  # Win
        else:
            chips -= bet  # Lose

    return cumulative_bets >= target


def simulate_games(num_games=10000):
    games_won = 0

    for _ in range(num_games):
        if play_game():
            games_won += 1

    win_rate = games_won / num_games

    print(f"Games simulated: {num_games}")
    print(f"Games won: {games_won}")
    print(f"Win rate: {win_rate:.2%}")


simulate_games()


# Drift-Diffusion Model (DDM):
    # Drift: The average direction of change
    # Diffusion: Random fluctuations around that average.

# A martingale argument is a proof technique in where the conditional 
# expectation of a future value, given all past information, equals the current value
