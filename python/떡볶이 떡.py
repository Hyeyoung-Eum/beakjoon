# N, M = map(int, input().split())
# c_list=list(map(int, input().split()))

# sum=0
# sum_list=[]
# for H in range(1, 1000):
#     for i in c_list:
#         sum+=i-H

#     if sum==M:
#         sum_list.append(H)
# print(max(sum_list))

# 19
# 15
# 10 17

n, m = map(int, input().split())
cake = list(map(int, input().split())) 

res=0
start=0
end=max(cake) #가장 긴 떡을 기준으로 잡음
while start<=end: #start가 end보다 커지면 중지한다.
    mid = (start+end)//2 #딱 중간 길이를 기준으로 잡음.
    total = 0
    for l in cake: #떡 list에서 하나씩 뽑아서
        if l>=mid: #만약 떡이 중간값보다 길면
            total+=l-mid #그 떡에서 중간값을 뺀 것을 total에 더한다.
    if total >= m: #total이 요구한 m값보다 크거나 같으면
        if mid > res: #만약 중간값이 result보다 크면,
            res=mid #중간값을 result로 만들어준다.
        start = mid+1 #그리고 출발지점을 중간값보다 1더 큰 것을 잡아준다.
    else:
        end = mid-1

print(res)