from collections import deque

n,m=map(int,input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    #q생성
    q = deque()
    q.append((x, y))
    
    #현재 위치 방문 처리
    paper[x][y]=0


    area = 1

    #q가 빌때까지 반복한다
    while q:
        x, y = q.popleft()

        #4가지 방향으로 다음 좌표를 만들고,
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #다음 좌표가 유효하면서, 아직 방문하지 않았으면
            if 0 <= nx <n and 0 <= ny <m and paper[nx][ny] == 1:
                q.append((nx,ny))
                paper[nx][ny] = 0
                area +=1
    
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
            max_area = max(max_area, bfs(i, j))
print(count)
print(max_area)

