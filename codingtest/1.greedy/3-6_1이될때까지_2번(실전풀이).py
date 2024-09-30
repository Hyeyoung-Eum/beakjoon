#n : 주어지는 수
#k : n을 1을 빼거나, k로 나누거나 둘 중에 하나만 할 수 있음.

n,k = map(int, input().split())
result = 0

while(True):
    #N==K로 나누어지는 수가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target) #1씩 빼는 횟수를 result 더해준다
    n=target #그리고 아래에서 계산을 위해 

    #while문 탈출구 : N을 K로 더이상 나눌 수 없을 때 반복문 탈출
    if n<k:
        break

    #K로 나누기
    result+=1
    n//=k


#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)