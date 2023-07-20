#플러그 빼는 횟수를 최소화하는 방법

#입력값
N, K = map(int, input().split())
order_list=list(map(int, input().split()))

#연산

#처음 3개는 그냥 받을 수 있음 -> 집합 형태 같음. 같은 원소는 상관없이 받음.
#3개를 넘어갈 때는, 새로운 수를 받을 때는 플러그 빼는 수 연산이 실행됨

multitap_set=set()
rst=0

def duplication():
    count_list=[]
    multitap_list=list(multitap_set)
    for j in multitap_list:
        count_list.append(multitap_list.count(j))

    multitap_list.remove(multitap_list[count_list.index(max(count_list))])
    rst+=1

for i in order_list:
    multitap_set.add(i)
    order_list.remove(i)
    if (len(multitap_set)==N):
        break

for i in order_list:
    if i in multitap_set:
        multitap_set.add(i)
        order_list.remove(i)
    else: #멀티탭에 꽂혀있지 않으면
        duplication()
        multitap_set.add(i)
        order_list.remove(i)

    #(만약 집합의 수가 3개가 되었으면 4번째 부터는
        #안에 있는 것과 같으면 그냥 넣기
        #다른게 나오면 집합 안에 있는 것들을 뒤에 남은 것에서 새서 이용수가 가장 적은 것 뽑기

print(rst)
#집합 특징
#인덱싱 X
#in으로 들어있는지 T/F출력 가능