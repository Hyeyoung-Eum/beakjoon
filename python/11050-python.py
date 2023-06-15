N, K = map(int, input().split())

def factorial(n):
    if n == 0 or n == 1 :
        return 1
    if n > 1:
        return n*factorial(n-1)

def combination(n, r):
    result = factorial(n)/(factorial(n-r)*factorial(r))
    return result

print(round(combination(N, K)))