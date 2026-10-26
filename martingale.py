
import random


def play_martingale_game():
    chips = 2000
    cumulative_bets = 0
    target = 10000

    while chips > 0 and cumulative_bets < target:
        # Dynamic bet: 10% of current chips
        bet = max(1, int(chips * 0.10))
        bet = min(bet, chips, target - cumulative_bets)

        cumulative_bets += bet

        if random.random() < 0.40:
            chips += bet
        else:
            chips -= bet

        # Target reached takes priority if both conditions
        # occur on the same bet.
        if cumulative_bets >= target:
            return True

        if chips == 0:
            return False

    return cumulative_bets >= target


def simulate_martingale(num_games=10000):
    wins = 0

    for _ in range(num_games):
        if play_martingale_game():
            wins += 1

    print(f"Games simulated: {num_games}")
    print(f"Games won: {wins}")
    print(f"Estimated win rate: {wins / num_games:.2%}")


simulate_martingale()
