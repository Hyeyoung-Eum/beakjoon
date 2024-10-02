def binary_search(arr, x):
    start = 0
    end = len(arr)-1
    mid = 0

    while start <= end:
        mid = (start + end )//2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x :
            end = mid -1
        else: #같으면
            return mid
    return -1 #못찾으면 -1반환