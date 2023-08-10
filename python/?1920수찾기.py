N=int(input())
N_list=list(map(int, input().split()))
M=int(input())
M_list=list(map(int, input().split()))

for i in M_list: #M_list의 요소들을 i로 하나씩 꺼내서
    #i가 N_list에 있는지 알아보자
    if i in N_list:
        print(1)
    else :
        print(0)