#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.
    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben")
        or None if a tie.
    """
    if not nums or x < 1:
        return None

    # Precompute primes using Sieve of Eratosthenes
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Count the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
