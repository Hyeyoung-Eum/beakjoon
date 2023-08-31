import sys
def input()->str:
    return sys.stdin.readline().rstrip()

n, m, b = map(int, input().split()) #세로 n, 가로 m, 인벤토리에 99개의 블록
heights=[list(map(int, input().split())) for _ in range(n)]

#블록을 추가하거나, 빼는 방법 2가지 경우 스킬 존재
#약간 체스판 자르기랑 비슷한 문제인 것 같다.

# 브루트포스로 모든 경우의 수를 구하고, 가장 시간이 적게 걸린 것 중,
# 땅의 높이가 높은 것 출력.

# 절대값 구하는 함수 abs()

ans = int(1e9) #답을 무한으로 걸어놓고, 조건을 만족시키면 바꿔준다.
glevel=-1
for h in range(0, 257):
    take_block=0
    use_block=0
    for i in range(n): #세로(row)
        for j in range(m):#가로(column)
            if heights[i][j]>=h: #추가
                take_block+=heights[i][j]-h
            else: #heights[i][j] <h:
                use_block+=h-heights[i][j]
    if use_block > take_block + b:
        pass
    else:
        t_sum=take_block*2+use_block

        if t_sum <= ans:
            ans = t_sum
            glevel=h #어차피 점점 높이가 높은 것으로 갱신 되니까
print(ans,glevel )