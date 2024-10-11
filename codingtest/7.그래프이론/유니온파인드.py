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
    if a < b:
        parent[b] = a
    else: # a > b
        parent[a] = b


#v: 노드의 개수, e: 간선의 개수
v, e = map(int ,input().split())

#부모 테이블 초기화 및, 본인 숫자로 초기화
parent = [0] * (v + 1) 
for i in range(1, v+1):
    parent[i] = i


#union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


###정답 출력 부분 ###

#각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')

print()

#부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=' ')