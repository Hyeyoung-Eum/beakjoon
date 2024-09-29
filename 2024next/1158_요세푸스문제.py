import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, k= map(int,input().split())

#턴 마다 출력시킬 사람에 해당하는 인덱스를 k-1로 초기화한다.
arr=list(range(1,n+1))

result=[]
queue = deque(arr)

while queue:
    #.rotate()함수를 사용하여 음수이면 왼쪽, 양수이면 오른쪽으로 deq이동
    queue.rotate(k*(-1))
    x=queue.pop()
    result.append(str(x))
    
print("<", ", ".join(result), ">", sep='')