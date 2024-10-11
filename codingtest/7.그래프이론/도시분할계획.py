#부모 찾기 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#합치기 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b


#n:집의개수, m:간선개수
v,e= map(int,input().split())

#부모테이블
parent=[0]*(v+1)
for i in range(1, v+1):
    parent[i] = i


edges=[]
result=0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
for edge in edges:
    cost, a, b = edge
    #사이클이 존재하지 않을 때만
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        last = cost #계속 업데이트 해서 결국 맨 마지막 값을 가짐

print(result - last)