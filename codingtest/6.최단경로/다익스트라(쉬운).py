import sys
input = sys.stdin.readline
INF = int(1e9) #10억 = 무한 의미

#노드의 개수, 간선의 개수 입력받기
n, m = map(int,input().split())
#시작 노드 번호
start = int(input())

#1.노드 연결 정보 그래프 : 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [ [] for i in range(n+1) ]
#2.방문 여부 리스트 : 방문한 적 있는지 체크하는 목적 리스트 만들기
visited = [False ] * (n+1)
#3.최단 거리 테이블 : 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int,input().split())
    #a노드에서 b로가는 노드의 비용이 c이다.
    graph[a].append((b,c))

#방문하지 않은 노드들 중, 가장 최단 거리가 짧은 노드의 번호 반환
##근데 이게 연결된 노드라는 말이 있나? = 다익스트라는 이 부분 자연스럽게 해결 됨.
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드 초기화 및 방문처리
    distance[start]=0
    visited[start]=True

    #시작 노드의 연결정보로 최단 거리 테이블 업데이트
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #방문하지 않은 것 중, 거리가 가장 짧은 것 찾고 방문처리
        now = get_smallest_node()
        visited[now] = True

        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#다익스트라 알고리즘을 수행합니다.
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력합니다.
for i in range(1, n+1):
    #도달할 수 없으면, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있으면
    else:
        print(distance[i])


