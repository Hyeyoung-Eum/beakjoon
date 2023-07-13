###1번 방법 : for문 사용### 
# sentence=input()
# reverse_sentence=''
# for i in sentence:
#     reverse_sentence=i+reverse_sentence
# print(reverse_sentence)

###2번 방법 : list의 reverse()함수 사용###
# sentence=list(input())
# sentence.reverse() #변수를 사용하지 않아도, reverse된 것이 원래 리스트 이름으로 저장된다.
# reverse_sentence=''.join(sentence) 
# print(reverse_sentence)

###3번 방법 : revesed() 사용 ###
sentence=list(input())
reverse_list=reversed(sentence) #얘는 값 저장이 필요해서, 변수를 지정해줘야한다.
reverse_sentence=''.join(reverse_list)
print(reverse_sentence)