from collections import deque

# v:노드의 개수, e:간선의 개수
v,e = map(int, input().split())
#모든 노드에 대한 진입차수 리스트 0으로 초기화
indegree = [0] * (v+1)
#간선정보 담기위한 그래프 초기화
graph = [ [] for i in range(v+1)]

#방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    #진입 차수를 1증가
    indegree[b] += 1

def topology_sort():
    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque() #queue기능을 위한 deque라이브러리 사용

    #처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    
    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내고 결과에 추가
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()