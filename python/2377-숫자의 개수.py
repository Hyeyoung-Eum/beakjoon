num_list=[]
for i in range(3):
    num_list.append(int(input()))
#A, B, C라는 변수로 받을 수 있는 좋은 방법이 있을까?

result=list(str(num_list[0]*num_list[1]*num_list[2]))

for k in range(10):
    print(result.count(str(k)))

#리스트로 만들어서, 문자열로 체크했다.