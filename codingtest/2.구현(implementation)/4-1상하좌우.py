n=int(input())
x,y=1,1
plans=input().split()

#L, R, U, D에 따른 방향
dx = [0, 0,-1,1]
dy = [-1,1,0,0]
move_types=['L','R','U','D']

#입력받은 plan 하나씩 꺼내서,
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)): #한 바퀴 돌면서
        #L, R, U, D 중 맞는 plan 발견하면, 좌표 업데이트
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)