array=[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개 남으면 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #pivot보다 큰 데이터 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left +=1
        
        #pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -=1
        
        #엇갈리면 교체
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array , 0, len(array)-1 )
print(array)