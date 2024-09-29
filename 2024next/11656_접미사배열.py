import sys

def input():
    return sys.stdin.readline().rstrip()

sentence=input()
result_list=[]

for i in range(len(sentence)):
    result_list.append(sentence[i:])

result_list.sort()

for result in result_list:
    print(result)