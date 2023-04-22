#"Case #x: A + B = C"
import sys

n=int(input())

for i in range(n):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print('Case #',i+1,': ', A,' + ',B,' = ',A+B, sep='')