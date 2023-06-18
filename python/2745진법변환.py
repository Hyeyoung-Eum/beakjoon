A= list(input().split())
N=A[0]
B=int(A[1])

N_list=list(N)
num_list=list(map(int, N_list))
base=1
result=0

for i in range(len(num_list)):
    result= result + num_list[len(num_list)-1-i] * base
    base=base*B

print(result)