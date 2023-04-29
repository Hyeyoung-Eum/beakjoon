list=list(range(1,31))
#list = [i for i in range(1, 31)] 이렇게도 가능
for _ in range(28):
    a = int(input())
    list.remove(a)

#처음 코드
# if list[0] <= list[1] :
#     print(list[0])
#     print(list[1])
# else :
#     print(list[1])
#     print(list[0])

#개선 코드
print(min(list))
print(max(list))


#리스트에다가 30번까지를 모두 넣어놓고, 입력이 들어오면 pop한다.
#입력이 들어오면, 그 숫자를 0에서 1로 변경하고, 여전히 0인 애들만 출력한다.