###첫 번째 queue를 활용한 풀이###
n, k = map(int, input().split())

#요세푸스 순열 생성
idx=0
queue= [i for i in range(1, n+1)]
res = []
while queue:
    idx += k-1 #k-1번째 인덱스까지 건너 뛰기
    if idx >= len(queue): #길이와 같아지는 부분부터 인덱스를 초과하기 때문
        idx %= len(queue) #idx = idx % len(queue)
    res.append(str(queue.pop(idx)))

print('<', ', '.join(res), '>', sep='')

###두 번째 deque를 활용한 풀이###
# from collections import deque

# n,k=map(int, input().split())

# #양방향 연결 리스트(deque) 생성
# deq = deque([i for i in range(1, n+1)])

# #요세푸스 순열 생성
# res=[]
# while len(deq) != 0:
#     for _ in range(k-1):
#         #k-1번째 노드까지 deq 맨 뒤로 이동
#         deq.append(deq.popleft())
#     #k번째 노드 삭제 후 결과 배열에 추가
#     res.append(str(deq.popleft()))
# #결과 출력
# print('<'+', '.join(res)+'>')