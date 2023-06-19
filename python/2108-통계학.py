N=int(input())

num_list=list()
while(len(num_list)!=N):
    num_list.append(int(input()))

avrg=round(sum(num_list)/len(num_list))

#중앙값 구하기
num_list.sort()
if len(num_list) % 2 == 0:
    middle=num_list[len(num_list)//2-1]+num_list[len(num_list)//2]
else:
    middle=num_list[len(num_list)//2]

#최빈값 구하기
a=0
basket={}
for i in range(len(num_list)-1):
    if num_list[i] == num_list[i+1]:
        a+=1
    else :
        basket[num_list[i]]=a

for c in basket.keys:
    print(c)

print(avrg)
print(middle)

