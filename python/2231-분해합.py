N=int(input())

x=0
for i in range(1, N+1):
    a=list(map(int, str(i))) #i를 list로 만들건데! int 형식으로 바꿀거야
    if N == sum(a) + i:
        x=i
        break;
print(x)
