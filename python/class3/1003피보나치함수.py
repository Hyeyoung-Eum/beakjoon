import sys

def input()->str:
    return sys.stdin.readline().rstrip()



# def fibonacci(x):
#     if x==0:
#         return 0
#     elif x==1:
#         return 1
#     else:
#         return fibonacci(x-1)+fibonacci(x-2)

t=int(input())

for _ in range(t):
    n=int(input())

    cnt_0=0
    cnt_1=0