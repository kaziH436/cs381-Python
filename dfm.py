
import random
import math


def play_ddm_game():
    chips = 2000.0
    cumulative_bets = 0
    target = 10000

    while chips >= 1 and cumulative_bets < target:
        # Dynamic bet: 10% of current chips
        bet = max(1, int(chips * 0.10))
        bet = min(bet, int(chips), target - cumulative_bets)

        if bet < 1:
            break

        cumulative_bets += bet

        # DDM: approximate the change with a normal distribution.
        drift = -0.20 * bet
        diffusion = math.sqrt(0.96) * bet

        chips += random.gauss(drift, diffusion)

        # Reaching the target takes priority over going broke
        # on the same bet.
        if cumulative_bets >= target:
            return True

        if chips < 1:
            return False

    return cumulative_bets >= target


def simulate_ddm(num_games=10000):
    wins = sum(play_ddm_game() for _ in range(num_games))
    print(f"DDM estimated win rate: {wins / num_games:.2%}")


simulate_ddm()
