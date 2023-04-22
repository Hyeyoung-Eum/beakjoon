#백준 14691 사분면 고르기

##처음에 작성해 본 코드
# input_x=int(input())
# input_y=int(input())

# if (input_x>0 and input_x<=1000):
#     if(input_y>0 and input_y<=1000):
#         print(1)
#     elif(input_y>=-1000 and input_y<0):
#         print(4)
# elif(input_x>=-1000 and input_y<0):
#     if(input_y>0 and input_y<=1000):
#         print(2)
#     elif(input_y>=-1000 and input_y<0):
#         print(3)

#조금 더 간결한 코드
x=int(input())
y=int(input())

if (x>0 and y>0):
    print(1)
elif (x<0 and y>0):
    print(2)
elif (x<0 and y<0):
    print(3)
else :
    print(4)