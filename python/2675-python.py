T=int(input())

for _ in range(T) :
    R, S = map(str, input().split())
    S_list=list(S)
    for i in S_list:
        print(i*int(R), end='')
    print('')