import sys
input=sys.stdin.readline

A, B = map(int,input().split())
m=int(input())
a_nums = list(map(int, input().strip().split()))
#1.10진수로 변환 시키는 과정 필요
###방법 : int(숫자,n진수)
#a_nums에서 하나씩 꺼내서 x자리에 넣고, 그것은 A진수이니, 10진수로 바꿔주세요. 그리고 a_nums_10에 넣어주세요
# a_nums_10=list(map(lambda x : int(x,A), a_nums))
decimal_value=0
for num in a_nums:
    decimal_value=decimal_value*A + num

#2.10진수를 n진수로 변환시키는 함수 작성
def convert_to_base(num, base):
    if num==0:
        return [0] #다른 return 값이 리스트이므로 [0]으로 통일
    digits=[]
    while num:
        digits.append(int(num%base))
        num=num//base
    return digits[::-1]
#3.a_nums_10 차례대로 넣어서 반환
b_nums=convert_to_base(decimal_value, B)
print(' '.join(map(str,b_nums)))
