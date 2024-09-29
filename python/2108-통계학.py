from collections import Counter

N=int(input())

num_list=list()
while(len(num_list)!=N): #N이 될 때까지 입력받기
    num_list.append(int(input()))

# #test
# num_list=[5,1,3,8,-2,2]

#1.평균 구하기
avrg=round(sum(num_list)/len(num_list))

#2.중앙값 구하기
num_list.sort()
if len(num_list) % 2 == 0: #숫자들이 짝수 개
    middle=round((num_list[len(num_list)//2-1]+num_list[len(num_list)//2])/2)
else: #숫자들이 홀수 개
    middle=num_list[len(num_list)//2]

#3.최빈값 구하기
cnt=Counter(num_list).most_common()
if len(cnt)>1 and cnt[0][1] == cnt [1][1]:
    mode=cnt[1][0]
else:
    mode=cnt[0][0]

print(avrg)
print(middle)
print(mode)
print(max(num_list)-min(num_list))