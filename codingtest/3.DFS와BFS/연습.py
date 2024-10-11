#dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[i]:
        if visited[i] == False:
            dfs(graph, i, visited)
    

v=9
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited=[False]*(v+1)

#bfs
from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end= ' ')

        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

#순열
def fac(n):
    result = 1
    for i in range(2, n+1):
        result = result*i
    return result

#조합
def comb(n, k):
    result=1
    if n < k :
        return 0
    if n==k or k==0:
        return 1
    if k > n/2:
        k=n-k
    for r in range(k):
        result = result * (n-r)//(r+1)
    return result

#heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

import math
print(math.gcd(2, 7))


#다익스트라
import heapq
import sys
input = sys.stdin.readline
INF= int(1e9)

n, m = map(int, input().split())
start = int(input())

#1.노드연결정보그래프
graph=[ [] for i in range(n+1)]
#2.최단거리테이블
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
