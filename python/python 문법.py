# #Q1.값을 가지는 인덱스를 알려줘!라고 할 때, 값이 중복되면?
# #A.앞의 인덱스를 출력한다.
# list=[2,2,3,3]
# cnt_list=[]
# set_list=set(list)

# for i in set_list:
#     cnt_list.append(list.count(i))
# print(cnt_list)
# print(max(cnt_list))
# print(list.index(max(cnt_list))) #겹칠 때는 앞에 인덱스를 뽑음

#Q2.python에서 특정 값을 찾고 싶을 때는 index로 찾아낸다.
list=[1,2,3,4,5]
print(list.index(2))
print(list.pop())
print(list)