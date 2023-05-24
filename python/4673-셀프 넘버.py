def d(n):
    sum=0
    for i in list(str(n)):
        sum+=int(i)
    result = n + sum
    return result

none_selfnumber=set()
for x in range(10001):
    result=d(x)

    none_selfnumber.add(result)
    while result<=10000:
        result=d(result)
        if result in none_selfnumber:
            break
        none_selfnumber.add(result)
        print("계산중")

for elem in range(1, 10001):
    if elem not in none_selfnumber:
        print(elem)