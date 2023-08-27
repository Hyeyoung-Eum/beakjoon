###직관적인 풀이(내가 푼 풀이)###
import sys
input=sys.stdin.readline
n=int(input())

#봉지는 3kg, 5kg 존재. n을 맞춰서 줘야함

#만약 정확하게 만들 수 없다면 에러처리 -1 출력

q5=n//5 #5로 나눴을 때 몫
r5=n%5 #5로 나눴을 때 나머지
# print('처음 q5 r5:', q5, r5)
if r5 ==0: #5로 나누어 떨어지면 최고! 가장 적은 봉지 수 필요
    print(q5) #몫 출력하고 끝
else: #5로 나누어 떨어지지 않으면
    q3=r5 // 3
    r3=r5 % 3
    if r3 ==0: #3으로 나누어 떨어지면 2번째 best case
        print(q5+q3)
    else:
        while(q5>0):
            q5=q5-1
            r5=r5+5

            q3=r5 // 3
            r3=r5 % 3

            # print('현재 q5 r5 q3 r3:',q5,r5,q3,r3)
            if r3 ==0:
                print(q5+q3)
                break
        if r3 !=0:
            print(-1)



###참고 풀이###
#: 5의 배수가 될 때까지 3을 빼주는 방식으로 처리

# sugar = int(input())

# bag=0
# while sugar >=0:
#     if sugar % 5 == 0 :
#         bag += (sugar //5)
#         print(bag)
#         break
#     sugar -=3
#     bag +=1 #5의 배수가 될 때까지 설탕 -3, 봉지 +1
# else:
#     print(-1)