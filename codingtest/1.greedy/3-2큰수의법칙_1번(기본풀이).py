n,m,k=map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

#k만큼 더하고, second 한 번 더해주고 반복
while True:
    #k만큼 더하고
    for i in range(k):
        if m==0:
            break
        result += first
        m -=1

    #second 한 번 더해주고
    if m == 0:
        break
    result += second
    m-=1

print(result)