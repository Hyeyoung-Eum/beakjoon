#첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력

#list를 이용한 풀이
N=int(input())
num_list=list(map(int, input().split()))

max=max(num_list)
min=min(num_list)
print(min, max)

# # #.sort()매소드 이용 - 하지만 출력 초과 됨! 문제 의도는 위에였던 것 같다.
# N=int(input())
# num_list=list(map(int, input().split()))
# num_list.sort()
# print(num_list)
# print(num_list[0], num_list[N-1])