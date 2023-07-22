# w_list=list(input())

# rst=0
# for w in w_list:
#     if w=='A' or w=='B' or w=='C':
#         rst+=3
#     elif w=='D' or w=='E' or w=='F':
#         rst+=4
#     elif w=='G' or w=='H' or w=='I':
#         rst+=5
#     elif w=='J' or w=='K' or w=='L':
#         rst+=6
#     elif w=='M' or w=='N' or w=='O':
#         rst+=7
#     elif w=='P' or w=='Q' or w=='R' or w=='S':
#         rst+=8
#     elif w=='T' or w=='U' or w=='V':
#         rst+=9
#     elif w=='W' or w=='X' or w=='Y' or w=='Z':
#         rst+=10

# print(rst)

###2번째 방법 : list를 만들 필요가 없다 그냥 반복문으로 처리 ###

dial_list=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
w=input()

rst=0

for unit in dial_list:
    for i in unit:
        for x in w:
            if i == x:
                rst += dial_list.index(unit) + 3

print(rst)