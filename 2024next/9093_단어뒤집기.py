import sys

input=sys.stdin.readline

T=int(input())
for _ in range(T):
    input_list=input().split()
    for word in input_list:
        print(word[::-1], end=' ')
    print()
