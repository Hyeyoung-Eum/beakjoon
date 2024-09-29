import sys

def input():
    return sys.stdin.readline().rstrip()


n=int(input())

#입력받은 수열을 하나의 리스트에 담기
sequence = [int(input()) for _ in range(n)]

#스택에 push하는 순서는 반드시 오름차순을 지킨다.(일단 그 숫자까지 넣고 판단한다는 뜻)
stack=[]
result=[]
current = 1
possible = True

#해당하는 것들 모두 넣기
for number in sequence:
    while current <= number:
        stack.append(current)
        result.append('+')
        current+=1
    
    #같으면 pop, 존재하지 않으면 불가능
    if stack and stack[-1] == number:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print('NO')