import sys

def input():
    return sys.stdin.readline().rstrip()

T=int(input())

#괄호문제로직
#1.(면 append하고 )면 pop한다.
#2.남은 (가 있거나, stack이 비었을 때 pop하면 아님.
for _ in range(T):
    vps=True
    cmd=input()
    stack=[]
    for i in cmd:

        if i == '(':
            stack.append(i)

        elif i== ')':
            if len(stack) ==0:
                vps=False

                break
            else:
                stack.pop()

    if len(stack) == 0 and vps==True:
        print('YES')
    elif len(stack) !=0 or vps==False:#남은 것이 있으면
        print('NO')
