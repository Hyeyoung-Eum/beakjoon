N=int(input())

num_list=list(map(int, input().split()))
prime_num_list=list()

if N != len(num_list):
    print('숫자의 개수가 맞지 않습니다. 다시 실행하세요')
else :
    #소수의 개수 구하는 코드
    #소수 : 1과 자기 자신만을 약수로 가진다.
    for n in num_list:
        a=0
        for i in range(1, 1000):
            if n % i == 0:
                a+=1
        if a == 2:
            prime_num_list.append(n)
    
    # print(prime_num_list)
    print(len(prime_num_list))