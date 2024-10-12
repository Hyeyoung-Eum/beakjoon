num_list = list(map(int, input()))

mid = len(num_list)//2
left = num_list[:mid] #4개면 2-1까지 즉, 0,1이 들어감
right = num_list[mid:] #4개면 2,3이 들어감

if sum(left)==sum(right):
    print("LUCKY")
else:
    print("READY")
