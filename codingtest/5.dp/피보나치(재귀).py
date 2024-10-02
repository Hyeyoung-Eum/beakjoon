#미리 빈 공간 파두기
d = [0]*100

def fibo(x):
    #종료 조건
    if x==1 or x==2:
        return 1
    
    #계산한 적 있으면 그 값 반환
    if d[x] != 0:
        return d[x]
    
    #계산한 적 없으면 점화식
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))