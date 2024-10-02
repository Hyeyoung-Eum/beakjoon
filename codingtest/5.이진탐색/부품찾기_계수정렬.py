#가게에 있는 부품들 입력받기
n=int(input())
n_list=list(map(int,input().split()))


#값을 인덱스 넘버로 취급할 수 있도록, 0으로 채워진 list생성.
array = [0] * 1000001
#가게에 있는 전체 부품 번호를 입력받아서 있으면 값을 0에서 1로 업데이트 한다. 인덱스 업데이트는 시간복잡도 1수준이라 엄청 효율적임.
for i in n_list:
    array[i] = 1

#손님이 찾는 것 입력받기
m=int(input())
m_list=list(map(int,input().split()))


#인덱스로 접근해서 존재하면 yes, 없으면 no 출력.
for i in m_list:
    if array[i] == 1:
        print('yes', end= ' ')
    else:
        print('no', end=' ')