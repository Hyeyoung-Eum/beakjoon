#괄호 균형 판단 프로그램
#(), []

import sys
input = sys.stdin.readline
play=True
while(play==True):
    line = input()
    small=0#괄호가 열리면 +1, 닫히면 -1
    large=0
    for i in line[:-1]:
        if i == '(':
            small+=1
        elif i==')':
            small-=1
            if small <0:
                print('no')
                break
        elif i=='[':
            large+=1
        elif i==']':
            large-=1
            if large <0:
                print('no')
                break
        else:
            pass
    else:
        if line[-1]=='.':
            break

    if small == 0 and large == 0:
        print('yes')
    else:
        print('no')