import sys

def input()->str:
    return sys.stdin.readline().rstrip()

M=int(input())

S=set()
for _ in range(M):
    answer_list=input().split()
    if len(answer_list)==2:
        cmd=answer_list[0]
        num=int(answer_list[1])
    else:
        cmd=answer_list[0]

    if cmd =='add':
        S.add(num)
    elif cmd =='remove':
        S.discard(num)
    elif cmd =='check':
        if num in S:
            print(1)
        else: #num not in S
            print(0)
    elif cmd =='toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif cmd =='all':
        S={i for i in range(1,21)}
    elif cmd =='empty':
        S=set()
    else:#error
        print('error처리')
    
