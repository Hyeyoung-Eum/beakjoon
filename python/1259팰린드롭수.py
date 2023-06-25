#팰린드롬수 우영우

while(True):
    n=input()
    if int(n) == 0:
        break
    else:
        n_list=list(n)
        bool_list=[]
        
        for i in range(len(n_list)-1):
            if n_list[i] == n_list[len(n_list)-1-i] :
                bool_list.append(True)
            
        if len(bool_list)>=len(n_list)-1:
            print('yes')
        else:
            print('no')

# #다른풀이
# while True:
#     n = input()

#     if n == '0':
#         break
    
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')