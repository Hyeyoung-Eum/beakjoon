import sys
input=sys.stdin.readline

N, M=map(int, input().split()) #N이 행, M이 열
board=[list(input()) for _ in range(N)]

#경우에 따라 색을 다시 칠한 횟수를 담는 리스트 만들어놓고, min() 출력하기.
rewrite_nums=list()


#8*8로 잘라서, 색을 최대한 적게 칠해도 되는 것 출력.
#시작점 잡아야 함.
for a in range(N-7):#+1은 인덱스 특성상, 1개를 덜 세기 때문에
    for b in range(M-7):
        idx1=0 #시작점B
        idx2=0 #시작점W
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 ==0: #i+j가 짝수면 시작점과 색이 같아야함
                    if board[i][j] != 'W':
                        idx1+=1
                    if board[i][j] != 'B':
                        idx2+=1
                else: #i+j가 홀수면
                    if board[i][j] != 'B':
                        idx1+=1
                    if board[i][j] !='W':
                        idx2+=1
        rewrite_nums.append(min(idx1, idx2))
print(min(rewrite_nums))