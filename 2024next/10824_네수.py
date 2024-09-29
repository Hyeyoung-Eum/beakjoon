import sys

def input():
    return sys.stdin.readline().rstrip()

A, B, C, D = input().split()

print(int(A+B)+int(C+D))