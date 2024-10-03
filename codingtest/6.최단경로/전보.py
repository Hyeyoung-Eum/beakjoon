import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph=[ [] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,input().split())
    #x번 노드에서 y로 가는 비용이 z다
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #처리한 적 있으면
            continue
        
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#도달할 수 있는 노드의 개수
count = 0
#   도달할 수 있는 노드 중에서 가장 멀리있는 노드와의 최단 거리
max_distance=0
for d in distance:
    if d != 1e9:
        count +=1
        max_distance = max(max_distance, d)
#시작 노드는 제외해야하므로 count -1 출력
print( count -1, max_distance )