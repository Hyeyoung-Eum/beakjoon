#예외 케이스를 어떻게 모두 처리하지?라고 생각했는데, 일단 좌표로 값을 계산을 완료한 후,
#유효하지 않은 값을 가지는 것들은 예외 처리를 한다!

#현재 나이트의 위치 입력받기 : ex) a1 형태로 입력들어옴.
input_data=input()
row = int(input_data[1])
column = ord(input_data[0])-ord('a')+1

#나이트가 이동할 수 있는 8가지 방향 정의 : 아래, 오른쪽으로 갈 수록 양수.
#그림그려서 좌표 직접 찍어보기. 반시계 방향으로 좌표 썼음.
steps= [(-2, -1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대해 각 위치로 이동 가능한지 확인.
result = 0
for step in steps: #가능한 8가지에 대해서 모두 확인
    #이동하고자 하는 위치 확인 : row에는 step[0]를 더하고, column에는 step[1]를 더한다.
    next_row = row + step[0]
    next_column = column + step[1]

    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <=8:
        result +=1
print(result)