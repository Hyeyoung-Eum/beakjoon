#n : 배열의 크기 2<=N<=1,000
#m : 숫자가 더해지는 총 횟수 1<=M<=10,000
#k : 연속으로 더해질 수 있는 횟수 1<=K<=10,000
n,m,k=map(int, input().split())

#data입력 받고, 정렬해서 가장 큰 값과 작은 값 찾아주기
data=list(map(int,input().split()))
data.sort()
first=data[-1]
second=data[-2]

#가장 큰 수가 더해지는 횟수 계산
##count = (묶음의 수 = 총 연산 횟수//first k개와 second 1개를 더한 묶음의 크기) * k(묶음당 큰 수가 k개 있기 때문)
count = (m // (k+1))*k
count += m%(k+1)

#값 더하기. 
result=0
result += (count)*first
result += (m-count)*second

print(result)