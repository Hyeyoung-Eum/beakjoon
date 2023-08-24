import sys
input=sys.stdin.readline

k=int(input())
num_list=[]
for _ in range(k):
    x=int(input())
    if x != 0:
        num_list.append(x)
    else:
        num_list.pop()
print(sum(num_list))
