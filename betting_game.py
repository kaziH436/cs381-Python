def play_game(strategy):
    chips = 2000
    cumulative_bets = 0

    while chips > 0 and cumulative_bets < 10000:
        # 1. Choose a bet using the strategy
        bet = strategy(chips, cumulative_bets)

        # 2. Add the bet to cumulative betting volume
        cumulative_bets += bet

        # 3. Simulate the outcome
        if random number is less than 0.40:
            chips += bet
        else:
            chips -= bet
