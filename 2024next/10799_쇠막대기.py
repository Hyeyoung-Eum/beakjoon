def count_cut_pieces(brackets):
    stack = []  # 스택 초기화
    count = 0  # 잘려진 조각의 총 개수 초기화

    i = 0
    while i < len(brackets):
        if brackets[i] == '(':
            if i + 1 < len(brackets) and brackets[i + 1] == ')':
                # 레이저인 경우
                count += len(stack)  # 스택에 있는 쇠막대기만큼 조각 추가
                i += 1  # 레이저 다음 문자로 건너뜀
            else:
                # 새로운 쇠막대기의 시작인 경우
                stack.append('(')  # 스택에 추가
        else:
            # 쇠막대기의 끝인 경우
            stack.pop()  # 스택에서 제거
            count += 1  # 잘린 조각 하나 추가
        i += 1

    return count

# 입력받기
brackets = input().strip()

# 결과 출력
print(count_cut_pieces(brackets))
