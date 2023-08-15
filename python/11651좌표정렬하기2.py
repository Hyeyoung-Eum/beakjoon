import sys

input=sys.stdin.readline

n=int(input())
tuple_list=[]
for _ in range(n):
    a, b = map(int, input().split())
    tuple_list.append((a,b))

#그냥 출력하면, 입력한 그대로 출력한다.
#.sort()함수는 상대적으로 작은 메모리 값을 차지한다. nlogn
    #하지만 이것은 맨 앞의 요소를 기준으로 오름차순으로 정렬해준다.
    #기준값을 뒤의 요소로 설정하여 정렬하는 것도 공부해보기.

#일단 직접 정렬해보는 것도 해볼까?
    #직접 정렬보단, .sort()가 더 효율 좋을 걸?

new_list=sorted(tuple_list, key=lambda tuple: (tuple[1], tuple[0]))
#기준 값을 여러개 설정해주려면, 튜플로 조건을 걸어주면 된다.
for i in new_list:
    print(*i)




###두 번째 방법###
#그냥 입력을 받고, 튜플로 append할 때, (b, a)로 넣는다. 그리고 출력할 때는 (a, b)로 출력