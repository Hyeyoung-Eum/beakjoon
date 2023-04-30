n=int(input())
score_list=list(map(int, input().split()))
maximum=max(score_list)
new_score=[]
for i in score_list:
    new=(i/maximum)*100
    new_score.append(new)

average=sum(new_score)/len(new_score)

print(average)