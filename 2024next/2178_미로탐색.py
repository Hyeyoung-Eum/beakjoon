import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

matrix=[]
for _ in range(N):
    matrix.append(list(input()+"1"))
matrix.append(list("1"*M))

row=0
col=0

cnt=0
#처음 시작 부분
if matrix[row][col]=="1":
    cnt+=1
else:
    print('시작점 안맞음')

#그 뒤로 계속 체크
while(True):
    #중간 기록 점
    mark_row=row
    mark_col=col

    row+=1
    if matrix[row][col]=="1":
        cnt+=1
    elif matrix[row][col]=="0":
        row-=1
        col+=1
        if matrix[row][col]=="1":
            cnt+=1
        elif matrix[row][col]=="0":
            col-=1
            row+=1