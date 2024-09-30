from collections import deque

n,m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))


#이동할 네 방향 정의(상,하,좌,우)
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#bfs구현
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        #현재위치
        x, y = queue.popleft()
        #현재위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로 찾기 공간을 벗어난 경우 무시합니다.
            if nx<0 or ny<0 or nx >=n or ny >=m:
                continue #다음 반복문 수행

            #벽인 경우 무시합니다.
            if graph[nx][ny] == 0:
                continue

            #해당 노드가 처음 방문하는 노드일 때만 최단 거리를 기록합니다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    #문제에서 요구한 값을 리턴합니다. 이때 문제에서 n,m이라고 했지만 인덱스 넘버로 인해 우리는 n-1,m-1로 출력하면 됩니다!
    return graph[n-1][m-1]

print(bfs(0,0))