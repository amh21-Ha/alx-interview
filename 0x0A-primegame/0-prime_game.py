#!/usr/bin/python3

"""
Module: Prime Game

This module implements a game where two players alternately choose prime
numbers and remove their multiples, determining the winner.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Parameters:
    x (int): Number of rounds.
    nums (list): List of integers representing the size of the number sets
    for each round.

    Returns:
    str: Name of the player who won the most rounds or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Determine the maximum value in nums
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute prime numbers up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Play each round of the game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The total number of primes up to n determines the number of moves
        moves = prime_count[n]

        # Maria wins if the number of moves is odd, otherwise Ben wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
