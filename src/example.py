# CANARY-B
"""Trivial example with an off-by-one bug."""


def sum_first_n(n):
    """Return the sum of 1..n inclusive."""
    total = 0
    for i in range(n):  # BUG: off-by-one, should be range(n + 1)
        total += i
    return total
