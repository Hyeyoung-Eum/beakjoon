n,m=map(int,input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    #재귀함수이므로 먼저 예외처리를 해준다.
    if x<0 or x>=n or y<0 or y>=m:
        return 0
    if paper[x][y]==0:
        return 0
    
    #현재 위치 방문 처리
    paper[x][y]=0
    area = 1

    #4가지 방향에 대해서 다음 좌표를 만들고 그것에 대한  dfs를 실행한다.
    for i in range(4):
        nx = x + dx[i]
        ny = y+ dy[i]
        area += dfs(nx, ny)
    
    return area

dx=[-1, 1, 0, 0]
dy= [0, 0, -1, 1]

count=0
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            #새로운 그림을 발견하면, 개수를 증가시키고 넓이를 계산한다.
            count += 1
            max_area = max(max_area, dfs(i, j))
print(count)
print(max_area)

