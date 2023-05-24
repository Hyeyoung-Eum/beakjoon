k=int(input())

def fibonacchi(k):
    if k<=1:
        return k
    else :
        return fibonacchi(k-2)+fibonacchi(k-1)
    #앞에 수 + #뒤에 수
print(fibonacchi(k))