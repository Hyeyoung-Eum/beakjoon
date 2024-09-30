n=int(input())
student_list=[]
for _ in range(n):
    cmd=input().split()
    student_list.append([cmd[0], int(cmd[1])])

print(f'before={student_list}')
student_list.sort(key=lambda x : x[1])
print(f'after={student_list}')

for student in student_list:
    print(student[0], end=' ')