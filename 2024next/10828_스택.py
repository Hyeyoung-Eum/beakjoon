import sys
input=sys.stdin.readline

N=int(input())
stack=[]

for _ in range(N):
    cmd_list=input().split()


    if len(cmd_list) != 1: #쪼개졌다면, 올바른 변수에 할당해주기
        cmd, num = cmd_list
    else:
        cmd = cmd_list[0]

    #반복적으로 계산하므로 stack 크기 미리 계산
    length=len(stack)

    if cmd == 'push':
        stack.append(num)
    elif cmd == 'pop':
        if length !=0:
            print(stack.pop()) #pop은 해당 값을 꺼내면서 리턴
        else: #비었으면 -1출력
            print(-1)
    elif cmd == 'size':
        print(length)
    elif cmd == 'empty':
        if length !=0:
            print(0)
        else:
            print(1)
    elif cmd == 'top':
        if length !=0:
            print(stack[-1])
        else: #비어있으면
            print(-1)

    
