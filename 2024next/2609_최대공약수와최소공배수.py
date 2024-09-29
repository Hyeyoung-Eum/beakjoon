# 두 정수 a와 b를 입력받는다.
a, b = map(int, input().split())

# 최대공약수(GCD) 찾기
for i in range(min(a, b), 0, -1):  # min(a, b)부터 1까지 거꾸로 반복
    if a % i == 0 and b % i == 0:  # a와 b 모두를 나눌 수 있는 가장 큰 수를 찾음
        print(i)  # 찾으면 출력
        break  # 찾은 후 루프를 종료

# 최소공배수(LCM) 찾기
for i in range(max(a, b), (a * b) + 1):  # max(a, b)부터 a*b까지 반복
    if i % a == 0 and i % b == 0:  # a와 b 모두로 나눌 수 있는 가장 작은 수를 찾음
        print(i)  # 찾으면 출력
        break  # 찾은 후 루프를 종료
