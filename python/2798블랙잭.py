N,M=map(int, input().split())

card_list=list(map(int, input().split()))

result_list=[]
for i in card_list:
    for j in card_list:
        for k in card_list:
            sum=i+j+k
            if sum <=M:
                if (i!=j)and(i!=k)and(j!=k):
                    result_list.append(sum)

print(max(result_list))