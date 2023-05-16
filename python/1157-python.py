#가장 많이 사용된 알파벳 뽑기
word=input().upper()
word_list=list(word)
word_set=list(set(word))

cnt=[]
for i in word_set:
    cnt.append(word_list.count(i))

if cnt.count(max(cnt))>1:
    print('?')
else :
    print(word_set[cnt.index(max(cnt))])