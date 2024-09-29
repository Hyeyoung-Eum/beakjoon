import sys
input=sys.stdin.readline

N, B = input().split()
B=int(B)
decimal_value=0
for num in N:
    #int(num,B) = B진법 num을 10진수로 바꿔줘.
    decimal_value = decimal_value * B + int(num, B)
print(decimal_value)