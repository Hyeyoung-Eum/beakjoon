#M이상 N이하의 소수를 모두 출력하기
#에라토스테네스의 체(소수 구하기: 소수 검사는 구하는 수의 제곱근까지만 해도 됨)
import sys
input=sys.stdin.readline
m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1 :
        continue
    for j in range(2, int(i**0.5)+1): #특정수의 제곱근까지만 확인해주면 됨.
        if i % j ==0:
            break
    else:
        print(i)

    

########시간초과 코드########
# import sys
# input=sys.stdin.readline

# m, n = map(int, input().split())

# for i in range(m, n+1):
#     cnt=False #합성수 수
#     for j in range(2, 1000001):
#         if i % j ==0 and i !=j:
#             cnt=True
#     if cnt == False:
#         print(i)
########시간초과 코드########