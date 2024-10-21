memo = {0:1, 1:1}

def fac(n):
    if n in memo:
        return memo[n]
    result = 1
    for i in range(2, n+1):
        result *= i
    
    memo[n] = result
    return result