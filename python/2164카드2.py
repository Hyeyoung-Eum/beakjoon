#pop(x) : x번째 요소를 리턴하고 그 요소를 삭제한다.
#list보다는 queue가 훨씬 성능이 좋다.


###처음 구현했던 시간초과 코드###
# import sys
# input=sys.stdin.readline
# N=int(input())
# cards=[a for a in range(1, N+1)]

# while (len(cards)>1):
#     #맨 앞(=위) 카드 지우기)
#     cards.pop(0)
#     if len(cards)==1:
#         break
#     #맨 앞(=위) 카드 맨 뒤로 옮기고, 맨 앞은 지우기)
#     cards.append(cards.pop(0)) #맨 앞의 것을 뽑아서 뒤에다가 추가.

# print(cards[0])

###deque로 구현한 코드###
import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
cards=[i for i in range(1,N+1)]
cards=deque(cards)

while(len(cards)>1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])


