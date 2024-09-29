import sys

input=sys.stdin.readline
n=int(input())
deque=[]

for _ in range(n):
    input_list=input().split()
    command = input_list[0]
    if len(input_list)==2:
        num=int(input_list[1])
    
    if command =='push_front':
        deque.insert(0,num)
    elif command =='push_back':
        deque.append(num)
    elif command =='pop_front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif command =='pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif command =='size':
        print(len(deque))
    elif command =='empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif command =='front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif command =='back':
        if not deque:
            print(-1)
        else:
            print(deque[len(deque)-1])
