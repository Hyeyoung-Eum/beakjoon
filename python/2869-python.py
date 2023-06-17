import math
A, B, V = map(int, input().split())

# #day
# day=1
# result=0

# #반복문으로 풀면, 시간 초과가 걸리는 문제이다.
# while(True):
#     result=result + A
#     print(day, '올라가요',end='')
#     print(result)
#     if result >= V:
#         break

#     result = result - B
#     print(day, '내려가요',end='')
#     print(result)
#     day+=1

n=(V-B)/(A-B)

print(math.ceil(n))
