import sys
def input()->str:
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
#n 듣도 못한 사람의 수
#m 보도 못한 사람의 수

people=[]

for i in range(n+m):
    people.append(input())
num=0
find_people=[]
while(len(people)!=0):
    tem_people=people[0]
    if people.count(tem_people)==2:
        find_people.append(tem_people)
        del people[0]
        num+=1
    else: #개수 하나
        del people[0]
print(num)
find_people.sort()
for j in find_people:
    print(j)