def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i+1 #타겟의 인덱스+1로 몇 번째 위치인지 반환해줌.