INF = int(1e9)

#n:노드개수, m:간선개수
n,m = map(int ,input().split())

#n*n 그래프 만들고 모두 무한으로 초기화
graph = [ [INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

#간선의 정보 m개 입력 받아서 1로 만들기
for _ in range(m):
    a, b = map(int,input().split())
    #양쪽 다 연결 되어있음
    graph[a][b] = 1
    graph[b][a] = 1

#거쳐 갈 노드 x와 최종 목적지 노드 k 입력받기
x, k = map(int,input().split())

#점화식에 따라 플로이드워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = graph[a][k] + graph[k][b]

#수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

#도달할 수 없는 경우
if distance >= INF:
    print("-1")
else:
    print(distance)