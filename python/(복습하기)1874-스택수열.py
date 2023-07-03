#push 순서는 반드시 오름차순
N=int(input())
stack=[]
answer=[]
flag=0
cur=1

for i in range(N):
    n=int(input())
    while (cur <= n): #입력한 수와 같아질 때까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur +=1

    if stack[-1]==n:
        stack.pop()
        answer.append("-")
    else: #stack의 TOP이 입력한 수가 아니면, 주어진 스택을 만들 수 없다.
        print("NO") #왜냐하면 TOP이 num보다 크면, num은 TOP보다 더 아래에 쌓여있기 때문이다
        flag=1
        break

if flag ==0:
    for i in answer:
        print(i)