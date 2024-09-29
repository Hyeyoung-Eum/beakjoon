import sys
input=sys.stdin.readline

#1.N보다 작은 소수들을 리스트에 담아 반환하는 함수
def sieve_of_eratosthenes(n):
    #모두 소수라고 가정
    is_prime=[True]*(n+1)
    p=2
    while(p*p<=n):
        if is_prime[p]:#만약 소수면, 배수들을 False로 설정
            for i in range(p*p, n+1,p):
                is_prime[i]=False
        p+=1
    return [p for p in range(2, n+1) if is_prime[p]]#2부터 시작으로, 0과 1은 예외처리

#2.위의 소수 목록에서 나누다가 안나눠지면 다음 소수로 넘어감
n=int(input())
prime_list=sieve_of_eratosthenes(n)

for prime in prime_list:
    if n==1:
        break
    while(n%prime==0):
        print(prime)
        n=n//prime

