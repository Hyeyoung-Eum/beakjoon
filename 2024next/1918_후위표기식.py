def infix_to_postfix(expression):
    # 연산자 우선순위 설정
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    result = []  # 후위 표기식을 저장할 리스트

    for char in expression:
        if char.isalpha():  # 피연산자(알파벳)인 경우
            result.append(char)  # 결과에 바로 추가
        elif char == '(':  # 여는 괄호인 경우
            stack.append(char)  # 스택에 추가
        elif char == ')':  # 닫는 괄호인 경우
            # 여는 괄호를 만날 때까지 스택에서 꺼내어 결과에 추가
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 여는 괄호 제거
        else:  # 연산자인 경우
            # 현재 연산자보다 우선순위가 높은 연산자를 모두 스택에서 꺼내어 결과에 추가
            while stack and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            stack.append(char)  # 현재 연산자를 스택에 추가

    # 스택에 남아 있는 모든 연산자를 결과에 추가
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# 입력 받기
expression = input().strip()

# 후위 표기식으로 변환
postfix_expression = infix_to_postfix(expression)

# 결과 출력
print(postfix_expression)
