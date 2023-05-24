#괄호 개수 판별 문제 stack활용문제

#몇 번 반복할 것인지 묻는다.
n=int(input())
stack=list()
#(가 들어오면, push()
def push(a):
    stack.append(a)
    print(stack)

#)가 들어오면, stack에서 pop()
def pop():
    stack.pop()
    if len(stack)==0:
        print('오류입니다')



for i in range(n):
    c_list=list(input())
    for j in c_list:
        if j == '(':
            push(j)
        elif j == ')':
            pop()

    if (len(stack)==0) :
        print('YES')
    else :
        print('NO')