import sys

def input():
    return sys.stdin.readline().rstrip()

def cnt(s,n):
    if n < s:
        return 0
    cnt=0
    while n>=s:
        cnt +=n//s
        n=n//s
    return cnt

n,m = map(int,input().split())
two_cnt = cnt(2,n) - cnt(2,n-m) - cnt(2,m)
five_cnt = cnt(5,n) - cnt(5,n-m) - cnt(5,m)

print(min(two_cnt,five_cnt))