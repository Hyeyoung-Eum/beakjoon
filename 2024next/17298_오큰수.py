def find_nges(arr):
    n = len(arr)
    result = [-1] * n  # 결과를 저장할 리스트, 초기값은 -1
    stack = []  # 스택 초기화

    for i in range(n):
        # 현재 원소가 스택의 맨 위 원소가 가리키는 원소보다 클 때까지 반복
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]  # 스택에서 꺼낸 인덱스의 오큰수를 현재 원소로 설정
        stack.append(i)  # 현재 원소의 인덱스를 스택에 추가

    return result

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 오큰수 찾기
result = find_nges(arr)

# 결과 출력
print(" ".join(map(str, result)))
