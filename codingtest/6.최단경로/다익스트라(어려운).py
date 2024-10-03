import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start=int(input())

#1.노드연결 정보그래프
graph = [ [] for i in range(n+1)]
#2.방문여부리스트X

#3.최단거리테이블
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 거리는 0으로 설정하며, 큐에 삽입
    heapq.heappush( q, (0, start) )
    distance[start] = 0
    while q : #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        #현재 노드가 이미 처리된 적 있으면 무시(작은 값 가진다는 것이 결국 처리된 적 있다는 뜻. 처리 안됐으면 INF일 것이기 때문에 무조건 클 수 밖에 없다. )
        if distance[now] < dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
        #i점을 거쳐가는 비용이 distance[i[0]] 원래 기록된 거리 비용보다 더 작으면, 업데이트
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] ==INF:
        print("INFINITY")
    else:
        print(distance[i])