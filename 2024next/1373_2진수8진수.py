#2진수가 주어졌을 때 8진수로 변환하는 프로그램!
 
import sys

def input():
    return sys.stdin.readline().rstrip()

#숫자를 3개씩 잘린 조각들로 만들어주는 함수
def make_pieces(num_string):
    #길이 계산
    length=len(num_string)
    remainder_length=length % 3
    share = length//3
    #3개로 딱 나뉠 수 있는 것들만 구분하여 새로운 문자열 생성
    new_string=num_string[remainder_length:]

    #share+1인 이유는, ramainder+share 횟수
    pieces=[]
    now=0
    for i in range(share+1):
        if i==0:
            remainder=num_string[0:remainder_length]
            pieces.append(remainder)
        else:
            a_piece=new_string[now:now+3]
            pieces.append(a_piece)
            now+=3
    return pieces

#조각들을 넣으면, 2진수를 8진수로 바꿔주는 함수
def two_to_eight_converter(pieces):
    result_list=[]
    for num in pieces:
        num_length=len(num)
        mid_result=0
        for i in range(num_length):
            mid=str(int(num[i])*(2**(num_length-1-i)))
            mid_result=mid_result+int(mid)
        result_list.append(str(mid_result))
    result=int(''.join(result_list))
    return result



num_string=input()
pieces=make_pieces(num_string)
result=two_to_eight_converter(pieces)
print(result)


    
        

