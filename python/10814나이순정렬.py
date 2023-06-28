import sys
N= int(sys.stdin.readline())

arr=[]

for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    arr.append([int(a),b])

arr.sort(key=lambda x:x[0]) #x[0]을 기준으로 x(요소들)을 정렬한다.

for i in arr:
    print(*i, sep=" ")

# # 시간 초과 코드
# N=int(input())
# member_list=[]
# for _ in range(N):
#     row=list(input().split())
#     member_list.append(row)

# for i in range(N):
#     print('현재 i', i, member_list[i])
#     for j in range(N):
#         print('현재 j', j, member_list[j])
#         if int(member_list[i][0])<int(member_list[j][0]): #제일 뒤에 숫자가 앞의 숫자보다 작으면 앞으로 올거야
#             member_list[i], member_list[j] = member_list[j], member_list[i]
#             print('교체된  member_list:', member_list)

# for a in member_list:
#     print(*a)

# # 낮은 순서대로 숫자 정렬 코드 연습
# N=int(input())
# n_list=list()
# for _ in range(N):
#     n_list.append(int(input()))
# a=0
# for i in range(N):
#     for j in range(N):
#         if n_list[i] < n_list[j]:
#             print(i,'와',j,'교체')
#             n_list[i], n_list[j] = n_list[j], n_list[i]
#             a+=1
#         print(n_list)

# print(n_list)
# print(a)
