word=input()
word_list=list(word)
b_list=[]
for i in range(round(len(word_list)/2)):
    if word_list[i] == word_list[len(word_list)-i-1]:
        b_list.append(True)

if  len(b_list) == round(len(word_list)/2):
    print(1)
else:
    print(0)