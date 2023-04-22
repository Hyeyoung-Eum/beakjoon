import sys

n=int(input())

for i in range(n):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)