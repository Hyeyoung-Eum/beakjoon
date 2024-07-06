
import sys

def input()->str:
    return sys.stdin.readline().rstrip()

#fibonacci의 결과를 우리가 구해야하는 횟수로 처리해버림
memo={0:(1,0), 1:(0,1)}

def fibonacci(n):
    #n이 0이거나 1이면
    if n in memo:
        return memo[n]
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        memo[n] = (a[0]+b[0],a[1]+b[1])
        return memo[n]

T=int(input())

for _ in range(T):
    N=int(input())
    result = fibonacci(N)
    print(result[0], result[1])