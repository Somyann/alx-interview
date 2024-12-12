#!/usr/bin/python3

"""
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
"""

def isWinner(x, nums):
    def sieve(max_n):
        """Generate a list of prime counts up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        # Precompute number of primes up to each index
        prime_count = [0] * (max_n + 1)
        for i in range(1, max_n + 1):
            prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
        return prime_count

    if not nums or x <= 0:
        return None

    max_n = max(nums)
    prime_count = sieve(max_n)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_removed = prime_count[n]
        # Maria wins if the number of primes removed is odd
        if primes_removed % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
