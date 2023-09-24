#그리디 알고리즘 사용
#가지고 있는 동전 중에서, 큰 단위가 항상 작은 단위의 배수여야만 그리디 알고리즘 적용 가능
#작은 단위의 동전을 종합해서 다른 해가 나올 수 없기 때문이다.
#앞의 선택이 이후의 선택에 영향을 주지 않고, 전체 문제를 부분적으로 해결할 수 있다면 그리디 의심!
import sys
def input()->str:
    return sys.stdin.readline().rstrip()

n, k=map(int,input().split())
#n개 가치 단위 동전들을 활용하여 합 k를 만들 것이다.

a_list=[]
for _ in range(n):
    a_list.append(int(input()))
i=-1
cnt=0
while(k!=0):
    now_won = a_list[i]
    cnt += k // now_won
    k %= now_won
    i-=1
print(cnt)