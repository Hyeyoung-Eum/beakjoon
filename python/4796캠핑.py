while(True):
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0 :
        break
#L일 동안 연속 P일 중 휴가는 V일 짜리 
    n=0
    while(L<V):
        if L<P:
            n+=L
            V=V-P

    if L<P and L>V:
        n+=V
    
    print(n)