def minimax_strategies(strategies):
    bestStrategy = None  # Initialize the best strategy variable
    bestValue = float('-inf')  # Start with the lowest possible value for comparison

    for strategy, outcomes in strategies.items():
        minOutcome = min(outcomes)  # Get the minimum outcome for this strategy
        if minOutcome > bestValue:  # Compare it to the best value found so far
            bestValue = minOutcome  # Update the best value
            bestStrategy = strategy  # Update the best strategy

    return bestStrategy, bestValue  # Return the best strategy and its value


if __name__ == "__main__":
    # Define business strategies and their potential outcomes
    business_strategies = {
        "Strategy A": [100, 200, -50, 150, 300],
        "Strategy B": [80, 50, 100, -20, 40],
        "Strategy C": [200, 300, 150, 0, 25],
        "Strategy D": [-100, -150, -50, 0, 10],
        "Strategy E": [400, 500, 100, 300, -100],
        "Strategy F": [50, 25, 30, -10, 5],
        "Strategy G": [300, -100, 200, 100, 250],
        "Strategy H": [0, 150, 200, -50, -100],
        "Strategy I": [250, 100, 50, -25, 10],
        "Strategy J": [300, 250, 200, -50, 100],
    }

    # Evaluate strategies
    bestStrategy, bestValue = minimax_strategies(business_strategies)
    print(f"The best strategy is: {bestStrategy} with a worst-case outcome of: {bestValue}")