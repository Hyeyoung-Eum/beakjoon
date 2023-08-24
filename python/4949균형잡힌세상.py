#괄호 균형 판단 프로그램
#(), []

import sys
input=sys.stdin.readline
#readline은 공백도 받으므로, rstrip()로 공백 제거.
while(True):
    tf=0 #오답이 확정일 때 -1로 구분지어주는 역할.
    
    line = input().rstrip() #입력 받기

    #<괄호의 균형을 맞춰야하는 문제 해결 방법>
        #가장 최근에 열린 괄호가, 자신의 짝과 일치하는지 확인한다.
            #일치하지 않으면 break
            #일치하면 그 색을 뽑아버린다.
    stack=[]
    
    if len(line)==1 and line[-1]=='.':#.이 들어오면 정지
        break

    else:
        for i in line:
            if i == '(' or i=='[':
                stack.append(i)
            elif i==')':
                if len(stack)==0 or stack[-1] !='(':
                    tf=-1
                    break
                else:
                    stack.pop()
            elif i==']':
                if len(stack)==0 or stack[-1] !='[':
                    tf=-1
                    break
                else:
                    stack.pop()

    if len(stack)==0 and tf!=-1:
        print('yes')
    else:
        print('no')

#마지막에 .을 넣어도 끝나지 않음
    #=> while문 안의 for문이 아니라, for문 시작 전에 if break문을 넣어줬음.
#print()를 해보면 no가 나옴.