#순서대로 Queue FIFO에 따라 인쇄 진행
#숫자가 높을 수록 높은 중요도
#Queue에서 앞에서부터 인쇄하는데, 중요도가 최고가 아니면 맨 뒤로 보낸다.
k=int(input())

for _ in range(k):
    n, m = map(int, input().split())
    #n=문서의 개수, m=m번째에 놓인 문서는 몇 번째(result)로 인쇄됩니까?
    importance_list=list(map(int, input().split())) #중요도 순서가, 문서 순서임.
    # print('importance_list:',importance_list)
    print_list=[]
    #1) 출력 순서를 나열한 뒤, m을 찾아서 출력 순서를 계산하는 방법 : 어떻게 같은 숫자 속에서도 m을 찾을 수 있을까? -> 처음 시작할 때부터, 색을 발라준다. 방법은 연구 필요. dict 유력함.
    #2) 중요도 list랑 프린트 대기열에 넣는 리스트 따로 파서, 맞으면 append. 그리고 아예 지우는게 아니라 숫자를 0으로 만들어주자.
    i=0
    while(len(print_list)<len(importance_list)):
        if i==len(importance_list):
            i=0 #7개면, 인덱스 넘버는 6까지 존재한다. 따라서 7이 되었다면, -7로 0으로 만들어줘야함.
        # print('현재 i값은:', i)
        # print('현재 importance_list[i]의 값은 :', importance_list[i])
        if importance_list[i] != -1: #이미 지나간 것은
            pass #그냥 지나가고, 얼른 다음 것 진행한다.
            #아닌 것은 정상적으로 진행한다.
        if importance_list[i] == max(importance_list):
            print_list.append(i) #index넘버를 기록한다.
            importance_list[i]=-1 #그리고 중요도를 -1로 바꿔준다.
        else:
            #실제로 맨 뒤로 보내는게 아니라, 그냥 지나치고 다시 처음부터 도는데 중요도가 -1인 것들은 건너뛰면 된다.
            pass
        i+=1
        # print(importance_list)
    for i in print_list:
        if i == m:
            print(print_list.index(i)+1) #print_cnt에는 인쇄되는 인덱스번호가 기록되어 있으니, 그 번호의 인덱스 번호를 찾아내주면 된다.