#첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
# 둘째 줄에는 정수가 공백으로 구분되어져있다.
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
# 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

##처음 작성했던 코드
# n=int(input())
# num_list=input().split()

# if n != len(num_list) :
#     print('개수가 다르네요, 다시 실행하세요')
# else:
#     which_n=int(input())
#     k=0
#     for i in num_list :
#         if which_n == int(i):
#             k=k+1
#     print(k)


#공부 후 수정한 코드
n=int(input())
num_list = list(map(int, input().split())) #바로 리스트에 넣어주는 개념 알게 됨
which_n=int(input())

print(num_list.count(which_n))
