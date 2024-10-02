#n : 떡의 개수, m : 요청한 떡의 길이
n,m=map(int,input().split())

line_list=list(map(int,input().split()))

def binary_search(arr,x):
    start=0
    end=max(arr)
    result = 0

    while(start <= end):
        total = 0
        mid = (start+end)//2
        for line in arr:
            temp =line - mid
            if temp > 0 : #0보다 클 때 값을 더한다.
                total +=temp

        if total < x : #결과값이 요청했던 x값보다 작다면, 절단기 높이인 mid를 낮춰야겠지?
            end = mid - 1
        else: #result >= x
            result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result를 한 번 기록해준다.
            start = mid + 1 #그리고 높이를 올려서 또 시도해본다.
    return result

print(binary_search(line_list, m))