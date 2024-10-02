array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언 : 최댓값보다 1큰 값도 포함할 수 있는 리스트!
count = [0] * ( max(array) + 1)

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)): #갯수만큼
    for j in range(count[i]): #그 숫자의 카운트 만큼 출력
        print(i, end= ' ')