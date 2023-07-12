N=int(input())
dot_list=[]
for _ in range(N):
    x, y = map(int, input().split())
    dot_list.append((x,y))

dot_list.sort()

for i in dot_list:
    print(*i)