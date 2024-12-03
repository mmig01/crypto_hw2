import random
import sympy
from prob1.prob1_a import check_miller_rabin


def generate_safe_prime_candidate(bits):
    while True:
        # 1024 비트 이상의 소수 p를 찾음
        p = random.getrandbits(bits - 1) | (1 << (bits - 1)) | 1  # p는 홀수여야 하므로 마지막 비트는 1로 설정
        if check_miller_rabin(p):
            # q = 2p + 1 계산
            q = 2 * p + 1
            if check_miller_rabin(q):  # q가 소수라면
                return q, p




if __name__ == '__main__':
    bits = 1024  # 예시 비트 수
    safe_prime = generate_safe_prime_candidate(bits)
    if safe_prime:
        q, p = safe_prime
        is_real_prime = sympy.isprime(q)
        print(f"Generated Safe Prime q: {q}")
        print(f"Corresponding Prime p: {p}")
        print(f"Is q a real prime? {is_real_prime}")
    else:
        print("Safe prime generation failed.")

# Generated Safe Prime q: 224470527027036577030165096611490431408833575483417863131494443907115523626791927784514718954646227027573605956699207977129089099304224232854318290458022780307214753146332584138603880766684486520493576208355804644780099643649870587998976050351152240869595003122159581227457011920984219180291698129991620003083
# Corresponding Prime p: 112235263513518288515082548305745215704416787741708931565747221953557761813395963892257359477323113513786802978349603988564544549652112116427159145229011390153607376573166292069301940383342243260246788104177902322390049821824935293999488025175576120434797501561079790613728505960492109590145849064995810001541
