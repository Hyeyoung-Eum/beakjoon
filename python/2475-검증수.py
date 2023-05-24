def square(n):
    return n*n

num_list=list(map(int, input().split()))
square_list=list(map(square,num_list))

print(sum(square_list)%10)