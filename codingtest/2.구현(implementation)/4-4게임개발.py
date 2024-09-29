#장소는 1*1 크기의 정사각형으로 이루어진 N*M 직사각형
#맵의 칸은 (A,B)로 나타나진다.
#각 칸은 육지 또는 바다 둘 중 하나이며, 바다는 갈 수 없다.

#[캐릭터의 가능한 행동]
#1.현재 방향에서 왼쪽으로 90도 회전하고,
#   왼쪽 방향에 가보지 않은 칸이
        #있으면 한 칸 전진
        #없으면 pass(회전만 진행한 것임)
#만약 네 방향 모두 가본 칸이거나, 바다가 되어있으면 바라보는 방향은 유지하고 한 칸 뒤로 가고 1단계로 돌아간다.
    #단, 뒤쪽 방향이 바다라서 갈 수 없는 경우에는 움직임을 멈춘다.

#[입력]
#1. 맵의 세로 크기 n, 가로 크기 m
#2. 캐릭터 시작 좌표 x, y, 방향direction(0:북, 1:동, 2:남, 3:서)
#3. 맵의 육지(0), 바다(1) 여부가 공백과 함께 matrix로 주어짐

n, m = map(int, input().split())

#방문 위치를 저장하기 위한 맵 생성하고, 0으로 초기화
d = [ [0] * m for _ in range(n) ]

#현재 캐릭터의 x좌표, y좌표, 방향 입력 받기
x, y, direction = map(int, input().split())
#현재 입력한 좌표 방문 처리
d[x][y]=1

#전체 맵 정보 입력받기
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

#북동남서 정의하기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    #바깥에서 선언된 변수를 가지고 오기 위해 global 변수명 사용
    global direction
    direction -=1
    if direction == -1:
        direction = 3
        
#시물레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time +=1
    #네 방향 모두 갈 수 없는 경우
    if turn_time ==4:
        nx= x- dx[direction]
        ny= y- dy[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤로 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
#정답 출력
print(count)


#[출력]
#: 캐릭터가 방문한 칸의 수 출력
