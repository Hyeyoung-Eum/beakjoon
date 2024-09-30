#n : 주어지는 수
#k : n을 1을 빼거나, k로 나누거나 둘 중에 하나만 할 수 있음.

n,k=map(int, input().split())
result = 0


while n>=k:
    #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n%k !=0:
        n -=1
        result +=1
    #k로 나누기
    n //= k
    result += 1

#마지막으로 n이 0이 될때까지
while n>1:
    n-=1
    result+=1

print(result)