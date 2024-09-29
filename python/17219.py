import sys

def input()->str:
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
keys_dict=dict()
for _ in range(N):
    url, key = input().split()
    keys_dict[url]=key

for _ in range(M):
    which_url=input()
    result=keys_dict[which_url]
    print(result)