
while(True):
    num_list=list(map(int, input().split()))

    if sum(num_list) == 0:
        break
    else :
        max_num=max(num_list)
        num_list.remove(max(num_list))
        if max_num**2 == num_list[0]**2+num_list[1]**2:
            print('right')
        else:
            print('wrong')


# #리스트 전체로 뺄셈도 가능할까? => 불가능!
# a=['1']

# b=['1', '2']

# print(b-a)ㅌ