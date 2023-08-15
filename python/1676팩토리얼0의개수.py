# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지
# 0의 개수를 구하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())

def factorial(x):
    if x == 0 or x == 1:
        result = 1
        return result
    elif x > 0:
        result = x * factorial(x-1)
        return result
    else:
        print('프로그램을 다시 실행해주세요')


cnt=0

rst_list=list(str(factorial(n)))

for i in range(len(rst_list)-1, -1, -1):
    if rst_list[i]=='0':
        cnt+=1
    else:
        break

print(cnt)