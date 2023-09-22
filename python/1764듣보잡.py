import sys
def input()->str:
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
#n 듣도 못한 사람의 수
#m 보도 못한 사람의 수

people_who_dont_hear=[]
people_who_dont_see=[]

for i in range(n):
    people_who_dont_hear.append(input())

for j in range(n):
    people_who_dont_see.append(input())

intersection = list(set(people_who_dont_hear) & set(people_who_dont_see))
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)