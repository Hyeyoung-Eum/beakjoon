import heapq

n=int(input())
q=[]

for _ in range(n):
    m=int(input())

    if m==0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    elif m>=1:
        heapq.heappush(q, m)
