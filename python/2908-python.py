# 1) list와 reverse를 활용
first_list=input().split()
reverse_list=[]

for b in first_list:
    sum=''
    word_list=list(b)
    word_list.reverse()

    for a in word_list:
        sum=sum+a
    reverse_list.append(int(sum))

print(max(reverse_list))

# # 2) 인덱스를 활용한 방법
# a, b = input().split()
# a=int(a[::-1])
# b=int(b[::-1])

# if a>b:
#     print(a)
# elif b>a:
#     print(b)