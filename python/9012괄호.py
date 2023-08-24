#stack 원리 이용
#ps=ps_list[0]를 하고, del ps를 했을 때, ps_list[0]가 사라지지는 않는다.
#python에서는 변수에 다른 변수를 선언할 때, 주소값을 저장해오는 것이기 때문이다.

# n=int(input())
# for _ in range(n):
#     ps_list=list(input())
#     bool_list=[]
#     tf=False
#     for _ in range(len(ps_list)):
#         # print('현재 ps_list[0]:', ps_list[0])
#         if  ps_list[0]== '(':
#             bool_list.append(1)
#             # print('1 추가')
#             del ps_list[0]
#         elif ps_list[0] ==')': # ps ==')'인데 
#             if len(bool_list) == 0:#만약 bool_list가 비었는데, 또 닫으려고 한다면 tf=False로 바꿔주고 break처리.
#                 tf=False
#                 break
#             else:
#                 del bool_list[len(bool_list)-1] #가장 최근에 들어간 것 삭제(stack원리)
#                 del ps_list[0]
#                 # print('1 제거')

    
#     if len(bool_list) == 0 and len(ps_list)==0:
#         tf=True
#     elif len(bool_list) !=0:
#         tf=False
    
#     # print('현재 tf는',tf,'입니다.')
#     if tf == True:
#         print('YES')
#     else:
#         print('NO')



#stack에 (는 append, )는 pop
###더 쉬운 풀이###
n = int(input())

for _ in range(n):
    parenthesis=0
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j==')':
            if '(' in stack: #스택안에 괄호가 있으면, 가장 최근 것 뽑는 메소드 pop()활용.
                stack.pop()
            else: #스택에 괄호가 없을 경우
                parenthesis=1
                break
    if (len(stack)==0) and (parenthesis == 0): #존재여부는 len()==0으로 확인.
        print('YES')
    else: #전부 pop되지 않았거나, stack안에 (가 없으면
        print('NO')


