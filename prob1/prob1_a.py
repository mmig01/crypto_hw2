import random
import sympy
errorNum = []

def miller_rabin_test(n, a):
    if n <= 1:  # 1 이하의 숫자는 소수가 아님
        return False
    if n % 2 == 0:  # 짝수는 소수가 아님
        return False

    # Find m and k such that n-1 = 2^k * m
    m = n - 1
    k = 0
    while m % 2 == 0:
        m = m // 2
        k += 1

    # T = a^m mod n
    T = pow(a, m, n)
    # Check the initial condition
    if T == 1 or T == n - 1:
        return True

    # Iteratively square T and check conditions
    for _ in range(k - 1):  # We repeat k-1 times
        T = pow(T, 2, n)
        if T == n - 1:  # Passed this round
            return True
        if T == 1:  # Found a non-trivial square root of 1 (composite)
            return False

    # If no condition is satisfied, n is composite
    return False

# miller-rabin 에 대한 테스트
def check_miller_rabin(n):
    arr = [31, 73]  # Random bases for the test

    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # Perform Miller-Rabin test with `iterations` random bases
    for _ in range(len(arr)):
        a = random.choice(arr)
        if not miller_rabin_test(n, a):
            return False
    return True

def false_positive_probability(range_start, range_end):
    false_positive_count = 0
    trials = range_end - range_start

    # 2^20 ~ 2^21 에 대하여 소수인지 검증
    for cur in range(range_start, range_end):
        # miller_rabin 을 이용해 n이 소수인지 확인
        if check_miller_rabin(cur):
            # sympy 라이브러리를 사용하여 실제 소수가 아니라면 false positive 로 판정
            if not sympy.isprime(cur):
                false_positive_count += 1
                # false positive 인 경우 errorNum에 추가
                errorNum.append(cur)
            
    # false positive 비율 계산
    return false_positive_count / trials
def main():
    # 2^20과 2^21 사이의 범위에서 실험
    range_start = 2**20
    range_end = 2**21

    false_positive_rate = false_positive_probability(range_start, range_end)
    print(f"False-positive 빈도: {false_positive_rate * (range_end - range_start + 1)}")
    print(f"False-positive 확률: {false_positive_rate:.5f}")
    print(f"False-positive 숫자: {errorNum}")
    



if __name__ == "__main__":
    main()

