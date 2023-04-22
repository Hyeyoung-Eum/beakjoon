#입력수 N, X보다 작은 수 다 보여줘!

N,X = map(int, input().split())

num_list=list(map(int, input().split()))

if len(num_list) != N:
    print('입력한 숫자 수가 설정값과 다릅니다. 다시 시도해주세요')
else :
    small_list=[]
    for i in num_list:
        if i < X :
            small_list.append(i)
    print(*small_list)