import sys

#input
input=sys.stdin.readline

n=int(input())

queue=[]
for _ in range(n):
    value_list=list(input().split())
    if len(value_list)==2:
        df = value_list[0]
        x = int(value_list[1])
    else:
        df = value_list[0]


    if df == 'push':
        queue.append(x)
    elif df =='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]

    elif df =='size':
        print(len(queue))
    elif df=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif df =='front':
        if len(queue)!=0:
            print(queue[0])
        else:
            print(-1)

    elif df == 'back':
        if len(queue)!=0:
            print(queue[len(queue)-1])
        else:
            print(-1)
