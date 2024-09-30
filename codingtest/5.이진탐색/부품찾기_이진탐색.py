n=int(input())
n_list=list(map(int, input().split()))
m=int(input())
m_list=list(map(int,input().split()))

def binary_search(arr, x):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=(start+end)//2
        if arr[mid] > x :
            end = mid -1
        elif arr[mid] < x :
            start = mid + 1
        else: #찾았으면
            return 'yes'
        
    return 'no'

n_list.sort()
for i in range(m):
    print(binary_search(n_list, m_list[i]), end= ' ')