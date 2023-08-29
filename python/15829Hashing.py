#해시함수 : 임의의 길이의 입력을 받아서, 고정된 길이의 출력을 내보내는 함수

import sys
input=sys.stdin.readline

l=int(input().rstrip()) #문자열의 길이
string=input().rstrip() #문자열

r=31 #예시 소수 : 
m=1234567891 #예시 소수 : 나누는 수

sum=0
i=0
for chr in string:
    sum+=(ord(chr)-96)*(r**i)
    i+=1

result=sum % m
print(result)