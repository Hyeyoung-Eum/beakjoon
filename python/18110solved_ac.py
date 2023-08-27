import sys
input=sys.stdin.readline

#python의 round()함수는 5사5입. 반올림자리가 5일 때, 앞자리가 홀수이면 올림, 짝수이면 내림한다.
#따라서 우리가 일반적으로 사용하는 4사5입 반올림 함수를 따로 정의해서 사용해야 한다.

#[0,1][T/F] 뒤에가 T면 1을, F면 0을 출력한다.
#int는 앞에 자리만 남겨준다. 소수점은 버려준.

def round45(num):
    return int(num) + [0, 1][num - int(num) >=0.5]
n=int(input().rstrip())

if n==0:
    print(0)

else:
    ranks=[int(input().rstrip()) for _ in range(n)]

    #아무 의견이 없다면, 문제의 난이도는 0
    #의견이 하나 이상 있으면, 모든 난이도 의견의 30%절사평균
        #절사평균 : 가장 큰 값과 가장 작은 값을 제외하고 평균
        #30% 절사평균 : 위에서 15%, 아래서 15%를 제외하고 평균.
        #소숫점은 모두 반올림

    ranks.sort()
    wing=round45(n*0.15)
    sum=0
    # #인덱스 단위로 계산
    start=wing
    end=len(ranks)-wing
    for i in ranks[start:end]:
        sum+=i

    # print(ranks)
    # print('wing',wing)
    # print('start', start)
    # print('end', end)
    # print('sum',sum)
    average=round45(sum/(n-wing*2))
    print(average)