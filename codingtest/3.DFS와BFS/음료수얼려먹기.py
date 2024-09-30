
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에, 연결된 모든 노드들도 방문 처리
def dfs(x, y):

    #들어온 x,y가 범위를 벗어나면 즉시 종료
    if x<=-1 or x >=n or y<=-1 or y>=m:
        return False
    
    #아직 방문하지 않은 노드가 존재하면
    if graph[x][y] == 0:

        #해당노드를 방문처리합니다.

        graph[x][y]=1
        #그리고 연결된 상하좌우도 dfs로 돌면서 방문처리되도록 합니다.
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        #방문하지 않았던게 하나라도 있는거니까 True 값을 보내서, 나중에 main함수에서 count될 수 있게 합니다.
        return True 
    #방문하지 않았던게 하나라도 없는 것이므로, False 값을 보내서, 나중에 main함수에서 count될 수 없도록 합니다.
    return False

result = 0
for i in range(n):
    for j in range(m):
        #모든 위치에 대해 dfs수행
        if dfs(i,j) == True:
            result+=1
print(result)