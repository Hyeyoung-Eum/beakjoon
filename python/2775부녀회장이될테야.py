import sys

input=sys.stdin.readline

T=int(input())


for _ in range(T):
    k=int(input()) #k층. 단계. sigma 횟수. 0층이 요소. 1층=1번 시그마, 2층=2번 시그마
    n=int(input()) #n호. 해당 시그마에서 n번까지 더해야함.

    people = [i for i in range(1, n+1)] #0층 사람들 넣기

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))
        people= new.copy()
    # 3층의 1호는 1명 2호는 1+ 1+ (1+2) 3호는 1+ 1 + (1+2) + 1 + (1+2+3) 
    # 2층의 1호는 1명 2호는 1+ (1+2) 3호는 1+ (1+2) + (1+2+3)  (i까지의 합을 k숫자를 넣어 반복문)
    # 1층의 1호는 1명, 2호는 1+2명, 3호는 1+2+3명 (i까지의 합 i(i+1)/2)
    # 0층의 1호는 1명, 2호는 2명, 3호는 3명 (i명))

    #k=0 n=호수
    #k=1 n=1부터 호수까지의 합
    #k=2 n=1부터 호수까지의 합 , 호수-1까지의 합, 호수-2까지의 합

    # #재귀함수의 특성인 것 같은데 한 번 알아보자.
    # def fibonachi(n):
    #     if n==0 or n==1:
    #         return 1
    #     elif n>1:
    #         return fibonachi(n-2)+fibonachi(n-1)
    
                # print(k,'일 때',i,'번째')
            # print(k,'일 때 result=',result)
            # return result
    #이전것의 코드가 무엇인지 모르는 상황이 발생한다.
    #이럴 때는 앞으로 나아가는 코드를 짤 것.
    #floor가 k와 같아질 때까지

#matrix[k][n] = matrix[k][n-1]+matrix[k-1][n]
    # print(matrix[k][n-2]+matrix[k-1][n-1]) #0호가 없기 때문에, 1호를 0호로 바꿨음. 

    # #sigma k : 1층의 n호 요소.
    # def sigma(end):
    #     result=0
    #     for i in range(1, end+1): #i부터 n까지의 합.
    #         result +=i
    #     return result

    # #1층 n호 요소 출력
    # print(sigma(n))

    # #2층(k) n호 요소 출력
    # def sigma2(end):
    #     result=0
    #     for i in range(1, end+1): #1부터 n호수까지
    #         result += sigma(i)
    #     return result

    # print(sigma2(n))