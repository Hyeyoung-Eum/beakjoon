num_list=[]
for i in range(9):
    num_list.append(int(input()))
print(max(num_list))

s=1
for a in num_list:
    if a != max(num_list):
        s=s+1
    elif a == max(num_list):
        print(s)