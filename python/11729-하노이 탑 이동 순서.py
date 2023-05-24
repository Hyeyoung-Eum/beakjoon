N=int(input())

#num함수 정의
#총 수 : 2*(앞의 것)+1
def num(x):
    if x==1:
        return 1
    else:
        return 2*num(x-1)+1

#좌표 찍는 함수 정의
def move(a, b, c, n):
    if n==1:
        print(a, c)
    else :
        move(a, c, b, n-1)
        print(a, c)
        move(b, a, c, n-1)

#1.move에서 2를3, 3을2로 변경한 값
#2.그냥 (1,3) 항상 중간
#3. move에서 1을2, 2를1로 변경한 값

A=1
B=2
C=3

print(num(N))
move(A, B, C, N)