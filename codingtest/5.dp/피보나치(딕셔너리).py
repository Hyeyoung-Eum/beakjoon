# 메모이제이션을 위한 딕셔너리를 함수 외부에 정의
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        memo[n] = result
        return result

n = 10
print(f"Fibonacci({n}) = {fib(n)}")
