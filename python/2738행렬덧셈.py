N, M = map(int, input().split())
A=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
    
B=[]
for _ in range(N):
    row=list(map(int, input().split()))
    B.append(row)

##numpy로 접근하는 방법
# import numpy as np
# A=np.array(matrix1)
# B=np.array(matrix2)
# C=A+B
# for row in C:
#     print(*row)

for row in range(N):
    for col in range(M):
        print(A[row][col]+B[row][col], end=" ")
    print()