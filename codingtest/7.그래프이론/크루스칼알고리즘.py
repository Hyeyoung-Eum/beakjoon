#1.find함수 : 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    #루트 노드는 자신의 부모가 자신임. 루트노드를 찾을 때까지 위로 올라가며 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
#2.union함수 : 두 원소가 속한 집합을 합치기. 각 노드의 부모 노드를 받고,
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #더 작은 숫자로 합쳐주기.
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#v: 노드의 개수, e: 간선의 개수
v, e = map(int ,input().split())
#부모 테이블 초기화 및, 본인 숫자로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

#모든 간선을 담을 리스트와 최종 비용 담을 변수 선언
edges=[]
result = 0
#모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용순 정렬을 위하여 다음과 같이 넣기
    edges.append((cost, a, b))
#비용에 따라 간선 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a ) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)