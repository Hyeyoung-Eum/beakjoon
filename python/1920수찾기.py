###set을 이용한 풀이###
#list의 search는 O(n)이지만, set의 search는 O(1)이다.

# import sys

# input=sys.stdin.readline

# N=int(input())
# N_list=set(map(int, input().split()))
# M=int(input())
# M_list=list(map(int, input().split()))

# for i in M_list: #M_list의 요소들을 i로 하나씩 꺼내서
#     #i가 N_list에 있는지 알아보자
#     if i in N_list:
#         print(1)
#     else :
#         print(0)


###이진탐색을 이용한 풀이###
#이진탐색 : 값을 비교할 때마다 찾는 값의 범위를 절반씩 좁히며 탐색
#시간복잡도 : O(logn) 으로 순차 탐색보다 효율적이다.
#이진탐색 전에 반드시 자료를 정렬해야한다.

import sys

def binary_search(a, x):
    start = 0
    end = len(a) -1

    while start <= end:
        mid = (start+end) //2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else: # x < a[mid]
            end = mid - 1
    return 0

input = sys.stdin.readline
n=int(input()) 
a=list(map(int, input().split())) #비교하는 풀.
a.sort() #리스트 정렬

m=int(input()) 
x=list(map(int,input().split())) #비교하고자 하는 주인공들

for k in range(m):
    print(binary_search(a, x[k])) #a는 비교하는 풀, x[k]는 비교 주인공들