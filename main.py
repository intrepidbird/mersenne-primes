import math

def calculate_mersenne_primes(limit: int) -> list:
    """
    Calculates Mersenne primes up to a given limit.

    Parameters:
    - limit: int
        The upper limit for calculating Mersenne primes.

    Returns:
    - list:
        A list of Mersenne primes up to the given limit.

    Raises:
    - ValueError:
        Raises an error if the limit is too large.
    """

    if limit > 1000000:
        raise ValueError("The limit is too large. Please provide a smaller limit.")

    mersenne_primes = []
    for i in range(2, limit + 1):
        if is_mersenne_prime(i):
            mersenne_primes.append(i)

    return mersenne_primes


def is_mersenne_prime(n: int) -> bool:
    """
    Checks if a given number is a Mersenne prime.

    Parameters:
    - n: int
        The number to check.

    Returns:
    - bool:
        True if the number is a Mersenne prime, False otherwise.
    """

    if not is_prime(n):
        return False

    mersenne_number = 2 ** n - 1
    return is_prime(mersenne_number)


def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime.

    Parameters:
    - n: int
        The number to check.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Example usage:

try:
    limit = int(input("Enter the limit for calculating Mersenne primes: "))
    mersenne_primes = calculate_mersenne_primes(limit)
    print("Mersenne primes up to the limit:")
    print(mersenne_primes)
except ValueError as e:
    print(f"Error: {e}")
