import random
import sympy
from concurrent.futures import ProcessPoolExecutor


def miller_rabin_test(n, a):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False

    m = n - 1
    k = 0
    while m % 2 == 0:
        m = m // 2
        k += 1

    T = pow(a, m, n)
    if T == 1 or T == n - 1:
        return True

    for _ in range(k - 1):
        T = pow(T, 2, n)
        if T == n - 1:
            return True
        if T == 1:
            return False

    return False


def check_miller_rabin(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for a in range(2, min(20, n - 1)):  # Use a few random bases for testing
        if not miller_rabin_test(n, a):
            return False
    return True


def generate_safe_prime_candidate(bits):
    # Candidate for p: random odd number with the required bits
    p = random.getrandbits(bits - 1) | (1 << (bits - 1)) | 1
    if check_miller_rabin(p):
        q = 2 * p + 1
        if check_miller_rabin(q):  # Check if q is prime
            return q, p
    return None


def generate_safe_prime_parallel(bits, num_candidates=10):
    with ProcessPoolExecutor() as executor:
        # Generate multiple candidates in parallel using a simple wrapper function
        results = list(executor.map(generate_safe_prime_candidate, [bits] * num_candidates))

        # Return the first valid safe prime found
        for result in results:
            if result is not None:
                return result
    return None


def main():
    bits = 100  # 예시 비트 수
    safe_prime = generate_safe_prime_parallel(bits)
    print(f"Generated Safe Prime q: {safe_prime}")
    if safe_prime:
        q, p = safe_prime
        is_real_prime = sympy.isprime(q)
        print(f"Generated Safe Prime q: {q}")
        print(f"Corresponding Prime p: {p}")
        print(f"Is q a real prime? {is_real_prime}")
    else:
        print("Safe prime generation failed.")


if __name__ == '__main__':
    main()