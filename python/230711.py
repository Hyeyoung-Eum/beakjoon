def swap(n1, n2):
    return n2, n1

n = int(input())
d = [int(input()) for _ in range(n)]

for i in range(n): #n번 반복한다. 크기만큼 반복.(라운드는 크기만큼))
    for j in range(i,0, -1): 
        if d[j-1] > d[j]:
            d[j-1], d[j] = swap(d[j-1], d[j])
    print(*d)