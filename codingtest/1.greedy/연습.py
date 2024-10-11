from collections import deque

n,m,v=map(int, input().split())
graph=[ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False] *(n+1)

#재귀
def dfs(graph, v, visited):
    #시작점 방문 및 출력
    visited[v] = True
    print(v, end= ' ')

    #연결된 친구들 차례대로, 하나씩 쭉 가니까 dfs임.
    for i in graph[v]:
        #아직 방문 안했으면
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, v, visited)
print()

visited=[False] *(n+1)
#while
def bfs(graph, v , visited):
    #시작점 큐에 넣으면서 방문처리
    q=deque([v])
    visited[v] = True

    while q:
        #큐에서 가장 앞 것을 꺼낸 다음 실행하므로 출력.
        now = q.popleft()
        print(now, end=' ')
        #방문 안한 주변 애들을 차례로 q에다가 넣음. 그러니까 주변 애들먼저 탐색하는 bfs인 것임.
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i]=True

bfs(graph,v,visited)
print()



