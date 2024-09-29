import sys
from collections import deque

# 표준 입력을 읽어오는 함수
def input():
    return sys.stdin.readline().rstrip()

# 초기 문자열을 받아서 left_stack에 저장
left_stack = deque(input())
right_stack = deque()  # 커서 오른쪽 문자를 저장할 스택

# 명령어의 개수 입력
m = int(input())

# 명령어 처리
for _ in range(m):
    command = input().split()
    
    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:  # left_stack이 비어있지 않으면
            right_stack.appendleft(left_stack.pop())  # left_stack에서 pop하여 right_stack에 appendleft
    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:  # right_stack이 비어있지 않으면
            left_stack.append(right_stack.popleft())  # right_stack에서 popleft하여 left_stack에 append
    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if left_stack:  # left_stack이 비어있지 않으면
            left_stack.pop()  # left_stack에서 pop
    elif command[0] == 'P':  # 커서 왼쪽에 문자 추가
        left_stack.append(command[1])  # left_stack에 문자 append

# 결과 출력
print(''.join(left_stack + right_stack))  # left_stack과 right_stack을 결합하여 문자열로 변환 후 출력
