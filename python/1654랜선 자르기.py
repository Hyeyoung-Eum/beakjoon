import sys, math
input=sys.stdin.readline

k, n= map(int, input().rstrip().split())
#k개의 랜선
#를 n개로 모두 같은 길이로 만드세요
#n개를 만들 수 있는 랜선의 최대 길이 출력

lines=[int(input()) for _ in range(k)]

lines.sort(reverse=True) #오름차순으로 정리
    #lines는 내림차순 정렬 이후 건들이기 없기

cnt=0 #몇 번째 순회인지 확인
breaker1=False
breaker2=False
while(True):
    if breaker1 == True and breaker2 == True: #삼중반복문 탈출
        break
    #밖에서 Lines를 변형해준다.
    standard_lines = [math.floor(line*((0.5)**cnt)) for line in lines] #변경 가능한 조건
    for standard in standard_lines: #line은 나누는 기준 line
        #이중반복문 탈출
        if breaker1==True: 
            breaker2=True
            break

        q_sum=0 #만들어지는 그룹의 개수
        for line in lines:
            q=line //standard
            q_sum+=q
        if q_sum == n:
            print(standard)
            breaker1=True
            break
    cnt+=1