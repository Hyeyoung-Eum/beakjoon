C=int(input())

for _ in range(C):
    char_list=input().split()
    num_list=list(map(int,char_list))
    avrg=sum(num_list[1:])/num_list[0]
    cnt=0
    for i in num_list[1:]:
        if i > avrg:
            cnt+=1
    rate = (cnt/num_list[0])*100
    print(f'{rate:.3f}%')