N=int(input())

for _ in range(N):
    char_list=list(input())
    sum=0
    for i in char_list:
        if i == 'O':
            sum+=1
        elif i =='X':
            break
    print(sum)