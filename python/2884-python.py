#시간을 45분 빼준다.

# input_time=input().split()
# hour=int(input_time[0])
# min=int(input_time.split[1])

#위의 세 줄의 코드를 map() 함수를 사용하여 다음과 같이 변경 가능
H, M=map(int, input().split(' '))

sum_M=H*60+M-45

new_H=sum_M//60
if (new_H < 0):
    new_H= 24+new_H
new_M=sum_M%60

print(new_H)
print(new_M)