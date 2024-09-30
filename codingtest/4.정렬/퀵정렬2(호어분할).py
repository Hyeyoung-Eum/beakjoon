array = [5, 7, 9 ,0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #리스트 길이가 1보다 이하면 종료한다.
    if len(array) <=1:
        return array
    
    #처음 pivot은 첫 번째 원소
    pivot = array[0]
    #피벗을 제외한 리스트 tail 생성
    tail = array[1:]

    left = [x for x in tail if x <= pivot ]
    right = [x for x in tail if x > pivot ]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))