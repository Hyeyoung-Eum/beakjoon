n=int(input())
num_list= [int(input()) for _ in range(n)]

num_list.sort(reverse=True)
print(*num_list)

