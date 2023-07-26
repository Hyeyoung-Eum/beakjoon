N,M=map(int, input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(input()))

# num=(M-8)*(N-8)

# #인식할 수 있어야 함.

# num_list=[]
# for i in range(num):
#     for j in range(i+8): #시작점 지정
#         semi_matrix=matrix[j:j+8]
#     #시작점 옮겨가면서 8번만 계산해주면 됨.
#     num_list.append()
#     #그리고 최솟값 출력하면 됨

#종이에다가 그려보면서 풀어보기

#230723 새로운 풀이법 생각남



def wb_change(num):
    if num=='W':
        return 'B'
    else: #num=='B'
        return 'W'

start_point=list(matrix[0][0])[0]
cnt=0

print('start_point는', start_point)
#1)각 row들의 시작점을 먼저 결정해준다.
for i in range(0, N, 2):
    if start_point != matrix[i][0]:
        cnt+=1
        print(i,'번째 row[0] 변경', sep='')
        matrix[i][0] = start_point

    #index 초과 오류 해결코드
    index=i+1
    if index > N:
        index=i-2
        
    if start_point == matrix[index][0]:
        cnt+=1
        print(i+1,'번째 row[0] 변경', sep='')
        matrix[i+1][0] = wb_change(start_point)
#2)시작점을 기준으로 계산해준다.
for row in matrix:
    for i in range(M-1):
        if row[i] == row[i+1]:
            cnt+=1
            row[i+1]=wb_change(row[i+1])

#3) 결과 출력
for row in matrix:
    print(*row, sep='')
print(cnt)
#스타트 포인트에 따라서, 짝수행은 모두 같아야한다.
#for row in matrix[0:N:2]: