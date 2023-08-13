###1) 답은 맞지만 시간초과 코드###
#for문 안에서 index, find, count 함수 사용하면 시간복잡도는 O(n^2)
#.sort()의 시간복잡도는 퀵 정렬과 같은 진화된 정렬방식 사용으로 O(NlogN)의 시간복잡도를 가진다.

# import sys

# input=sys.stdin.readline
# n=int(input())
# cards=list(map(int, input().split()))
# M=int(input())
# w_cards=list(map(int, input().split()))

# for w_card in w_cards:
#     print(cards.count(w_card), end=' ')






###2) 답도 맞는 두 번 이진 탐색하는 코드###
# import sys

# input=sys.stdin.readline
# n=int(input())
# cards=list(map(int, input().split()))
# cards.sort()

# m=int(input())
# targets=list(map(int, input().split()))

# #mid에 찾고자 하는 숫자가 나와도 이진탐색을 계속하면서, 양쪽 끝의 index번호 반환.
# #왼쪽, 오른쪽 2번 필요.
# def down_binary(target):
#     left = 0
#     right = len(cards) -1

#     while(left <=right):
#         mid = (left+right) //2
#         if cards[mid] >= target:
#             right = mid -1 #타겟과 같아도 멈추지 않고, 계속 right를 왼쪽으로 한 칸씩 밀어서, 최종적으로 right가 left보다 작아질 때, left는 가장 왼쪽 인덱스 값.
#         elif cards[mid] < target:
#             left = mid + 1
#     return left

# def up_binary(target):
#     left = 0
#     right = len(cards) -1

#     while(left <=right):
#         mid = (left+right)//2
#         if cards[mid]>target:
#             right = mid -1
#         elif cards[mid] <=target:
#             left = mid + 1 #타겟과 같아도 멈추지 않고, 계속 left를 우측으로 한 칸씩 밀어서, 가장 오른쪽 인덱스를 가져오게 됨.
#     return left

# for i in range(m):
#     print(up_binary(targets[i])-down_binary(targets[i]), end=' ')

###dict()이용 풀이
#card 숫자들을 dict의 key, 카드 숫자의 갯수를 value로 하여 사전을 만들고
#target 숫자들을 key로 하여 value 출력

# import sys
# input=sys.stdin.readline

# n=int(input())
# cards=list(map(int, input().split()))
# cards.sort()

# m=int(input())
# targets = list(map(int, input().split()))

# dic=dict()

# for i in cards: #O(n)
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i] = 1

# for i in range(m):
#     if targets[i] in dic:
#         print(dic[targets[i]], end=' ')
#     else:
#         print(0, end=' ')








###3) collections의 Counter모듈 사용###
from collections import Counter
import sys
input=sys.stdin.readline

n=int(input())
cards=list(map(int, input().split()))
cards.sort()

m=int(input())
targets = list(map(int, input().split()))

cnt = Counter(cards)

for i in targets:
    print(cnt[i], end= ' ')