
from collections import deque

#위상정렬을 해야한다.

v=int(input())

degrees=[0] * (v+1)

graph=[ [] for _ in range(v+1)]

#각 강의 시간 테이블 생성
time = [0] * (v+1)

#방향 그래프의 간선 정보 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:#-1하면 맨 마지막 것 제외
        #본인한테 오는 연결이 몇 개인지 세어줌
        degrees[i]+=1
        graph[x].append(i)

#위상 정렬 함수
def topology_sort():
    result = [0] *(v+1)
    q = deque()

    for i in range(1, v+1):
        if degrees[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            degrees[i] -=1

            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if degrees[i] == 0:
                q.append(i)
        
    for i in range(1,v+1):
        print(result[i])

topology_sort()



