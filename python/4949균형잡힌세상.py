#괄호 균형 판단 프로그램
#(), []

while(True):
    tf=0
    line = input()
    small=0#괄호가 열리면 +1, 닫히면 -1
    large=0
    
    #문이 열릴 때마다,색을 칠해준다.
    #닫을 때 칠해진 색과 닫을 색이 일치하지 않으면 break
    #일치하면 그 색을 뽑아버린다.
    color=[]
    if len(line)==1 and line[-1]=='.':
        break
    else:
        for i in line:
            if i == '(':
                small+=1
                color.append('small')
            elif i==')':
                small-=1
                if small <0: #한 번이라도 이런 경우가 생기면 에러처리를 위해 tf=-1로 변경.
                    tf=-1
                    break
                if color[-1] !='small':
                    tf=-1
                    break
                else:
                    color.pop()
            elif i=='[':
                large+=1
                color.append('large')
            elif i==']':
                large-=1
                if large <0:
                    tf=-1
                    break
                if color[-1] !='large':
                    tf=-1
                    break
                else:
                    color.pop()

    if small == 0 and large == 0 and tf==0:
        print('yes')
    else:
        print('no')

#마지막에 .을 넣어도 끝나지 않음
    #=> while문 안의 for문이 아니라, for문 시작 전에 if break문을 넣어줬음.
#print()를 해보면 no가 나옴.ㄴ