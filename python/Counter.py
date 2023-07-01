#Counter연습

from collections import Counter

#0.기본개념 : 리스트를 넣으면, 딕셔너리 형태로 개수를 세어서 반환한다.
#1.인자
print(Counter(['a', 'b', 'a', 'c']))
print(Counter('hello'))

#2.변수에 넣어서 사용할 수 있다.
num_list=[1, 2, 3, 4, 5, 3, 2]
cnt=Counter(num_list)
print(cnt)

#내림차순 정리 메소드 : .most_common()
##튜플 형태로 반환한다.
print(cnt.most_common())
print(cnt.most_common()[0][0])