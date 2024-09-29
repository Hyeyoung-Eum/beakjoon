N, K = map(int,input().split())
result=0

while True:
    #(N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (N//K)*K #나누어 떨어지는 수 중 가장 큰 수
    #따라서 1을 빼는 횟수는 다음과 같이 빠르게 연산 가능하다.
    result+=(N-target)

    #N이 K보다 작아지면 멈출 것임
    if N < K:
        break
    #그러기 전까지 일단 계속 나눠주자.
    N=N//K
    result+=1

#N이 K보다 작은 상태이므로, 1이 될 때까지 계속 뺄 것임. 그래서 횟수에다가 그냥 1남길 때까지의 횟수를 더해버림.
result += N-1
print(result)