import sys

input=sys.stdin.readline
n=int(input())

rst=0
i=0
while (rst<n):
    i+=1
    if '666' in str(i): #i에 666이 포함되어 있으면,
        rst+=1 #번째를 올리기 위해 카운트 해줍니다.

    
if rst==n: #입력한 n번째 수와, rst 값이 같아지면 
    print(i) #해당 i값 출력