#a_{i} : i번째 식량창고까지의 최저의 해(얻을 수 있는 식량의 최댓값)
#k_{i} : i번째 식량창고에 있는 식량의 양. = array에 들은 값

n=int(input())

array=list(map(int, input().split()))

d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2, n):
    #i번째를 안채운 것과, i-2번째 그리고 i번째를 채운 것
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])