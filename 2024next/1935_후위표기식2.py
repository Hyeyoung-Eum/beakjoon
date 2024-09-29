# 표준 입력을 사용하여 데이터를 읽어오기 위해 sys 모듈을 임포트
import sys
input = sys.stdin.readline

# 피연산자의 개수를 입력 받음
N = int(input().strip())

# 후위 표기식을 입력 받음
postfix_expression = input().strip()

# 피연산자에 대응하는 값을 저장할 리스트
values = []
for _ in range(N):
    values.append(int(input().strip()))

# 후위 표기식 계산을 위한 스택 초기화
stack = []

# 후위 표기식을 순회하면서 계산 수행
for char in postfix_expression:
    if 'A' <= char <= 'Z':  # 피연산자인 경우
        # 피연산자에 대응하는 값을 스택에 추가
        stack.append(values[ord(char) - ord('A')])
    else:  # 연산자인 경우
        # 스택에서 두 개의 피연산자를 꺼내 연산을 수행
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

# 스택에 남아 있는 결과 값을 가져옴
result = stack.pop()

# 결과를 소수점 둘째 자리까지 출력
print(f"{result:.2f}")
