# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지
# 0의 개수를 구하는 프로그램을 작성하시오.

#1.factorial을 직접 재귀함수로 만들어서 계산
#2.import math as m 하고, m.factorial(n)으로 계산
#3.pypy3로 할 경우, 메모리 초과가 뜨기 때문에, 그냥 python3로 제출해야했음.
#4.마이너스 인덱싱하는 방법 익혀두기.

#1.factorial을 직접 재귀함수로 만들어서 계산
# import sys

# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# n=int(input())

# def factorial(x):
#     if x == 0 or x == 1:
#         result = 1
#         return result
#     elif x > 0:
#         result = x * factorial(x-1)
#         return result
#     else:
#         print('프로그램을 다시 실행해주세요')
        
# sep_n=list(str(factorial(n))) #n! 계산값을 문자열로 바꾸어서 리스트로 넣는다.

# cnt=0

# for i in range(1, len(sep_n)+1):
#     if sep_n[-i]=='0': #-1부터 ~-길이 만큼, 뒤에서부터 0이 있으면 개수 카운트
#         cnt+=1
#     else:
#         break
        
# print(cnt)


################################
#2. import math as m 로 m.factorial(n)을 활용하여 계산
import sys
import math as m

sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
sep_n = list(str(m.factorial(n)))

cnt=0

for i in range(1, len(sep_n)+1):
    if sep_n[-i]=='0': #-1부터 ~-길이 만큼, 뒤에서부터 0이 있으면 개수 카운트
        cnt+=1
    else:
        break
        
print(cnt)

################################
# 3.인수 중 2와 5의 개수를 찾아내서 계산
# import sys
# import math as m

# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# n=int(input())

# N1=m.factorial(n)
# N2=m.factorial(n)

# cnt=0
# while(N1>=5):
#     if N1 % 5 == 0 :
#         N1=N1//5
#         cnt+=1
#     else:
#         break

# cnt2=0
# while(N2>=2):
#     if N2 % 2 == 0:
#         N2=N2//2
#         cnt2+=1
#     else:
#         break

# print(min(cnt,cnt2))

################################
# 4.단순히 5의 개수를 찾아내서 계산(입력 값의 범위가 적기 때문에 가능)
#5의 개수를 찾으면 된다. 0이 늘어나는 순간은 10이 곱해지는 순간이기 때문.
#해당 범위 내에서는 5가 생기는 순간에서 2의 개수는 당연히 5의 개수보다 많기 때문에 이렇게 되는 듯.

# N=int(input())
# print(N//5 + N//25 + N//125)