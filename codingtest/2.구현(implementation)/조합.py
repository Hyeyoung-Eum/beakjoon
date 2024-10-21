memo = {}

def comb(n,k):
    if (n, k) in memo:
        return memo[(n,k)]
    
    if k > n:
        return 0
    
    if k==0 or n==k:
        return 1

    if k > n//2:
        k=n-k

    result = 1

    for r in range(k):
        result = result *( n - r ) // (r+1)
    
    memo[(n,k)] = result

    return result

n,k=8,3
print(comb(n,k))