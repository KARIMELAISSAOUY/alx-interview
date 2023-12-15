#!/usr/bin/python3
"""0. Minimum Operations
"""


def minOperations(n):
    """Calculates the minimum operations to get exactly n H characters in a file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: Minimum operations needed for n H characters, or 0 if impossible.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
