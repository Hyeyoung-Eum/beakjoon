num_list=list(map(int, input().split()))

asc=False
des=False

for i in range(7):
    if num_list[i]< num_list[i+1]:
        asc=True
    elif num_list[i]>num_list[i+1]:
        des=True

if asc==True and des==True :
    print('mixed')
elif asc==True:
    print('ascending')
elif des==True:
    print('descending')