from collections import deque

def bfs(graph, start, visited):
    #start를 queue에 넣고 방문 처리
    q = deque([start])
    visited[start] = True

    #큐가 빌 때까지 반복
    while q:
        
        #가장 먼저 들어간 것 꺼내서 출력
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:

            #아직 방문 안한 것 큐에 넣고 방문처리
            if not visited[i]:
                q.append(i)
                visited[i]=True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited= [False]*9