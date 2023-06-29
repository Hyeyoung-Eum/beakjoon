N=int(input())

w_list=[]
for _ in range(N):
    w=input()
    if w not in w_list:
        w_list.append(w)

#길이가 짧은 것부터 나열한다.
#1.단어별로 리스트로 만들어서 배열을 만든다.
array=[]
for i in w_list:
    array.append([len(list(i)),i])

array.sort()

# for j in array:
#     for i in range(50):
#         if j[0] == i:
#             print(j[1])

for i in array:
    print(i[1])
# 그 길이가 짧은 순서대로 배열한다. 

# ##다른 풀이
# N=int(input())
# w_list=[]

# for i in range(N):
#     w_list.append(input())

# set_list=set(w_list)
# w_list=list(set_list)
# w_list.sort()
# w_list.sort(key=len) #길이순으로 정렬
# for i in w_list:
#     print(i)