def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2] #pivot은 중간에 위치한 값이 됩니다.
    left = [ x for x in arr if x < pivot ]
    middle = [ x for x in arr if x == pivot]
    right = [ x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)