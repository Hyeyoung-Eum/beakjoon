N=int(input())

x_list=[]
y_list=[]
rank_list=[]

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)


for i in range(N): #i는 사람
    rank=1
    for j in range(N): #j는 비교하고자 하는 전체
        if (x_list[j] > x_list[i]) and (y_list[j] > y_list[i]):
            rank+=1
    rank_list.append(rank)

print(*rank_list)