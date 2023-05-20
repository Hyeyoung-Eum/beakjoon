N=int(input())

for _ in range(N):
    ox_list=list(input())
    score_list=[]
    score=0
    for i in ox_list:
        if i == 'O':
            score+=1
            score_list.append(score)
        elif i == 'X':
            score=0
    print(sum(score_list))