#a_i= 금액 i를 만들 수 있는 최소한의 화폐 개수
#k=각 화폐의 단위

#for문을 통해 각 화폐 단위인 k를 하나씩 확인하며,
#a_{i-k}를 만드는 방법이 존재하는 경우, a_{i} = min(a_{i}, a_{i-k}+1}
#a_{i-k}를 만드는 방법이 불가능한 것은, 그냥 못만든다는 것이므로 a_{i}=INF를 준다!

#시간복잡도 확인
#N은 100, M은 10,000이므로 곱해도 100만이다. N^2로 풀어도 해결 가능!

#화폐단위 별로 한 바퀴씩 돌린다.


#n은 화폐 개수, m은 목표 금액
n,m = map(int, input().split())

#n개의 화폐 정보 입력받기
array=[]
for i in range(n):
    array.append(int(input()))

#한 번에 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)

#DP진행(bottom-up)
d[0]=0
for i in range(n): #i는 현재 선택된 화폐의 인덱스를 의미하고(n이 화폐의 개수이므로)
    for j in range(array[i], m+1): #array[i]는 현재 선택한 화폐의 금액부터, 목표금액 m까지를 의미
        if d[j - array[i]] != 10001: #j는 확인하고 있는 금액, array[i]는 확인하고 있는 화폐 금액. i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]]+1) 

#계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])