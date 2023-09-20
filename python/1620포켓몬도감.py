import sys
def input()->str:
    return sys.stdin.readline().rstrip()

n,m=map(int, input().split())
#n : 포켓몬 개수 #m : 문제 개수

monster_list=[]
for i in range(n):
    monster_list.append(input())

for j in range(m):
    answer = input()
    #응답이 숫자인지 문자인지 구분 필요(앞글자의 아스키코드로)
    first=ord(answer[0])
    if  first>=48 and first<=57:
        print(monster_list[int(answer)-1])
    else: #문자면
        print(monster_list.index(answer)+1)