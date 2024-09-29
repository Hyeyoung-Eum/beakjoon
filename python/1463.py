# import sys

# input=sys.stdin.readline



# def makeone(x_list):
#     if x_list[0]%3==0:
#         x_list[0]=x_list[0]//3
#         return x_list
#     elif x%2==0:
#         x_list[0]=x_list[0]//2
#         return x_list
#     else:
#         x_list[0]=x_list[0]-1
#         return x_list
# x=int(input())
# x_list=[x]
# cnt=0
# while(x_list[0]!=1):
#     makeone(x_list)
#     print('현재x:',x_list)
#     cnt+=1

# print(cnt)
# #2로 나어서 1이 되는 경우
# #3로 나누어서 1이 되는 경우
# #

# #x=1, 1
# #x=2, 2

import sys

input = sys.stdin.readline

def min_operations_to_one(n):
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

x = int(input().strip())
print(min_operations_to_one(x))
