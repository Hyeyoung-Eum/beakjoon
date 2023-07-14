n = int(input())
d = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        print('i=',i,'j=', j)
        if d[i] < d[j]:
            d[i], d[j] = d[j], d[i]
        

print(d)