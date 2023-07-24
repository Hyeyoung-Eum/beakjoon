N=int(input())
cage=[]
for _ in range(N):
    cage.append([0,0])
print(cage)

#1개부터 N개까지 사자는 들어갈 수 있다.
    #사자를 넣는 만큼 N을 선택한다.

for i in range(1, N+1): #시그마 역할
    #조합으로 row를 선택한다.
    #N개 중 i개를 선택하는 경우의 수
    # comb=(N!)/((K!)(N-K))!
    num_list=list(range(1,i+1)) #i개의 숫자 중에서
#먼저 row줄을 선택한다.
