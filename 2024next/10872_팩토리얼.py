import sys

def input():
    return sys.stdin.readline().rstrip()

def factorial(n):
    if n<2:
        return 1
    result=1
    for i in range(2,n+1):
        result=result*i
    return result
N=int(input())
print(factorial(N))