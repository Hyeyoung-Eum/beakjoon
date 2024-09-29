import sys

def input():
    return sys.stdin.readline().rstrip()

A=input()
B=input()
C=input()

print(int(A)+int(B)-int(C))
print(int(A+B)-int(C))

