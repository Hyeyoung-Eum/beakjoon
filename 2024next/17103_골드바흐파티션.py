#에라토스테네스의 체를 사용하여 소수 목록 생성
def sieve_of_eratosthenes(max_num):

    #max_num까지의 모든 수를 소수로 가정
    ##(0도 있어서, 인덱스 번호 맞추기 위해 +1해서 생성)
    is_prime = [True] * (max_num + 1)
    p=2
    #p의 제곱이 max_num 이하일 때까지 반복(에라토스테네스의 체 개념임)
    while( p*p <= max_num):
        if (is_prime[p] ==True):
            #p의 배수들은 모두 소수가 아니라고 표시한다.
            ##p*p부터 시작하는 이유는, 이미 p*p보다 작은 수들은 이전에 지워졌음.
            for i in range(p*p, max_num + 1, p):
                is_prime[i]=False
        p+=1
    
    #0과 1은 소수가 아님
    is_prime[0], is_prime[1] = False, False
    #소수 목록 생성
    primes = [p for p in range(max_num + 1) if is_prime[p]]
    return primes, is_prime

#주어진 짝수 n에 대해 골드바흐 파티션의 수를 계산
def goldbach_partition_count(n, primes, is_prime):
    count = 0
    #소수 목록 순회
    for p in primes:
        #p가 n의 절반을 넘으면 중복 계산을 피하기 위해 종료
        if p > n//2:
            break
        # n-p가 소수인지 확인
        # n=p+q인데, q=n-p 에서 n-p가 소수면, q도 소수이기 때문!
        if is_prime[n-p]:
            count+=1
    return count

def main():
    import sys
    input=sys.stdin.read
    data=input().split()

    T=int(data[0])
    cases = [int(data[i]) for i in range(1, T+1)]

    max_num=max(cases)
    #에라토스테네스의 체를 사용하여, max_num까지의 소수 목록 생성
    primes, is_prime = sieve_of_eratosthenes(max_num)

    results=[]

    #각 짝수에 대해 골드바흐 파티션의 수를 계산
    for n in cases:
        count = goldbach_partition_count(n, primes, is_prime)
        results.append(count)
    
    #결과 출력
    for result in results:
        print(result)
if __name__=="__main__":
    main()