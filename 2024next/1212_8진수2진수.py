import sys

def input():
    return sys.stdin.readline().rstrip()

#각 숫자의 접두어
#2진수 : 0b (ex : 0b101010)
#8진수 : 0o (ex : 0o52)
#16진수 : 0x (ex : 0x2a)


#다른진수 문자열 'num'을 -> 10진수 변환
#int(num,원하는 진수 숫자 n ) : 해석 num은 n진수 숫자야. 10진수로 바꿔줘.

#10진수num->다른진수로 문자열로 변환
#2진수 : bin(num)
#8진수 : oct(num)
#16진수 : hex(num)

o=input()

#1.8진수를 10진수로 변환한다.
decimal=int(o,8)
#2.2진수로 변환한다.
bin=bin(decimal)
print(bin[2:])
