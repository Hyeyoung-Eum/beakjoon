list=[]
for _ in range(10):
    a = int(input())
    b = a % 42
    if b not in list :
        list.append(b)
print(len(list))