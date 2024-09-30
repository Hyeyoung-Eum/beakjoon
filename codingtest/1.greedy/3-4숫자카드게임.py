#문제
##한 행을 선택하고, 그 행의 최솟값을 출력한다. 이때 가능한 가장 큰 값 출력하기.

#입력
##n행 m열로 일단 n,m을 입력 받고
###다음 줄 부터 공백을 포함한 숫자들이 입력된다.

#배울점
##1.특정 최솟값이나 최댓값을 찾을 때, 리스트에 넣고 한 번 더 계산하는게 아니라, 값을 업데이트하면서 감.
##2.입력하여 들어오는 행 별로 값을 처리함.

n,m=map(int, input().split())
result=0
for _ in range(n):
    #행 입력 받음
    row=list(map(int, input().split()))
    #행의 최솟값 획득
    min_value=min(row)
    #더 큰 값으로 결과를 업데이트
    result=max(min_value, result)

print(result)