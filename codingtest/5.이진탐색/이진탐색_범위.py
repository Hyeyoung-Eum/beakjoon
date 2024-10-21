def find_first_greater(arr, target):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        # mid 값이 target보다 작거나 같으면, 범위를 오른쪽으로 좁힘
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start  # target보다 큰 값이 시작되는 인덱스

# 예시
arr = [1, 2, 3, 4, 5, 6, 7]
target = 6
index = find_first_greater(arr, target)

# 결과 출력
if index < len(arr):
    print(f"{target}보다 큰 값은 {arr[index]}부터 시작하며, 인덱스는 {index}입니다.")
else:
    print(f"{target}보다 큰 값이 없습니다.")

def find_last_less_or_equal(arr, target):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        # mid 값이 target보다 크면, 범위를 왼쪽으로 좁힘
        if arr[mid] > target:
            end = mid - 1
        else:
            # mid 값이 target보다 작거나 같으면, 범위를 오른쪽으로 좁힘
            start = mid + 1

    return end  # target보다 작거나 같은 값의 마지막 인덱스

# 예시
arr = [1, 2, 3, 4, 5, 6, 7]
target = 6
index = find_last_less_or_equal(arr, target)

# 결과 출력
if index >= 0:
    print(f"{target}보다 작거나 같은 값은 {arr[index]}이며, 인덱스는 {index}입니다.")
else:
    print(f"{target}보다 작거나 같은 값이 없습니다.")
