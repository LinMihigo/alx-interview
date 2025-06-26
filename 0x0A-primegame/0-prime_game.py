#!/usr/bin/python3


def is_prime_sieve(n):
    """Generate a list of booleans indicating if numbers <= n are prime.

    Args:
        n (int): The upper limit of the sieve.

    Returns:
        List[bool]: A list where index i is True if i is a prime, False otherwise.
    """
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """Determines the winner of multiple rounds of a prime number game.

    Players take turns choosing a prime number from the remaining set of
    consecutive integers starting from 1 to n, and removing that prime and all
    its multiples. The player unable to make a move loses the round.

    Maria always starts first. The game is repeated x times with different n
    values. The player with the most wins is declared the overall winner.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers, each representing n for a round.

    Returns:
        str or None: Name of the player with most wins ("Maria" or "Ben"),
                     or None if there is no winner.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_sieve = is_prime_sieve(max_n)

    # Precompute number of primes up to each i ≤ max_n
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if prime_sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
