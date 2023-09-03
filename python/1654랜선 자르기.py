import sys
def input()->str:
    return sys.stdin.readline().rstrip()

#이진탐색(이분탐색))
def binary_search(a_list, x):# a는 랜선 리스트, x는 입력한 n
    start=1 #가장 짧은 길이
    end=a_list[-1] #가장 긴 길이

    while(start<=end):
        print('현재 start=',start,'현재 end=', end)
        mid=(start+end)//2 #결국 최종적으로 mid가 문제에서 찾고자 하는 정답이 될 것임
        result=0
        print('현재 mid=',mid)
        for line in a_list:
            result+= line // mid
        print('현재 result=',result)
        if result >= x:
            start = mid+1
        elif result < x : #개수가 x보다 적으면,개수를 늘릴 수 있도록 해야하니까 정답인 mid를 더 작게 바꿔야한다.
            end = mid -1
        # else: #result > x: #개수가 x보다 많으면, 개수를 줄일 수 있도록 정답인 mid를 키운다.
        #     start= mid+1
    return end

k, n = map(int, input().split())
#k개의 랜선을 n개로 모두 같은 길이로 만드세요
#n개 만들 수 있는 랜선의 최대 길이 출력(answer)

lines=[int(input()) for _ in range(k)]

lines.sort() #오름차순으로 정리

print(binary_search(lines, n))


########시간초과 코드##########
# import sys, math
# input=sys.stdin.readline

# k, n= map(int, input().rstrip().split())
# #k개의 랜선을 n개로 모두 같은 길이로 만드세요
# #n개를 만들 수 있는 랜선의 최대 길이 출력

# lines=[int(input().rstrip()) for _ in range(k)] #랜선 길이 입력 받기

# lines.sort(reverse=True) #오름차순으로 정리
#     #lines는 내림차순 정렬 이후 건들이기 없기

# cnt=0 #몇 번째 순회인지 확인

# #다중반복문 탈출을 위한 불린변수 선언
# breaker1=False
# breaker2=False

# #핵심 코드 시작
# while(True):
#     #part1.삼중반복문 탈출 코드
#     if breaker1 == True and breaker2 == True: 
#         break
    
#     #part2. 길이가 긴 랜선부터, (0.5)**cnt 배씩 곱해준 기준 길이를 만들기 위해 반복문 수행

#     standard_lines = [math.floor(line*((0.5)**cnt)) for line in lines] #변경 가능한 조건
#     for standard in standard_lines: #line은 나누는 기준 line
#         #ex) 입력받은 lines=[802, 743, 539, 457]의 경우 standard는 순서대로 이렇게 됨.
#             # stardard 802
#             # stardard 743
#             # stardard 539
#             # stardard 457
#             # stardard 401
#             # stardard 371
#             # stardard 269
#             # stardard 228
#             # stardard 200 ...

#         #이중반복문 탈출
#         if breaker1==True: 
#             breaker2=True
#             break

#         q_sum=0 #만들어지는 그룹의 개수
#         for line in lines:
#             q=line //standard
#             q_sum+=q
#         if q_sum == n:
#             print(standard)
#             breaker1=True
#             break
#     cnt+=1

