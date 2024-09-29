#최대공약수
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

#최소공배수
def lcm(x, y):
    return (x * y) // gcd(x, y)

# 입력 받기
T = int(input().strip()) 
results = []  

for _ in range(T):
    A, B = map(int, input().strip().split())
    results.append(lcm(A, B)) 

# 결과 출력
for result in results:
    print(result)
