import sys
#오름차순정렬
#sort는 메모리를 재할당하여, 많은 수를 정렬할 때는 적합하지 않다

N=int(sys.stdin.readline())
num_list=[0]*10001 #리스트를 새롭게 만드는 방법이군!

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1 #입력된 숫자를 인덱스로 받아서, 해당하는 인덱스의 숫자를 0이 아닌 1로 만든다.

for i in range(10001):
    if num_list[i] != 0: #값이 0이 아닌, 1이상인 값들만 받아서
        for j in range(num_list[i]): #j번 만큼
            print(i) #i를(숫자의 인덱스)를 출력한다.