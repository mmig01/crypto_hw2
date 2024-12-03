# Naive 소수 판별법
import time
import math
import matplotlib.pyplot as plt

from prob1_a import check_miller_rabin

# Naive 소수 판별법
def naive_prime_test(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 시간 측정을 위한 함수
def measure_time(method, n, *args):
    start_time = time.time()
    method(n, *args)
    return time.time() - start_time

# 실행 시간 비교를 위한 실험
def compare_running_time(start, end, step):
    n_values = []
    naive_times = []
    mr_times = []

    for n in range(start, end, step):
        n_values.append(math.log2(n))

        # Naive 소수 판별법 실행 시간
        naive_time = measure_time(naive_prime_test, n)
        naive_times.append(naive_time)

        # Miller-Rabin 소수 판별법 실행 시간
        mr_time = measure_time(check_miller_rabin, n)
        mr_times.append(mr_time)

    return n_values, naive_times, mr_times

# 비교할 범위와 단계 설정
start_value = 2**20
end_value = 2**30
step_value = 2**5  # 2^5 간격으로 테스트

# 실행 시간 측정
n_values, naive_times, mr_times = compare_running_time(start_value, end_value, step_value)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(n_values, naive_times, label="Naive Prime Test", color="blue")
plt.plot(n_values, mr_times, label="Miller-Rabin Test", color="red")
plt.xlabel("log2(n)", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.title("Running Time Comparison: Naive vs Miller-Rabin", fontsize=14)
plt.legend()
plt.grid(True)
plt.show()