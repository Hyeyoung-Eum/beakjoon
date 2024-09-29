import sys

def input():
    return sys.stdin.readline().rstrip()

sentence=input()
sentence_list=list(sentence)

cursor = len(sentence)
for _ in range(int(input())):
    cmd_list=input().split()

    if len(cmd_list) == 2:
        #리스트 할당
        cmd, word = cmd_list
    elif len(cmd_list) ==1:
        cmd = cmd_list[0]
    

    if cmd == 'L':
        cursor-=1
        if cursor <0:
            cursor=0
        print(f'현재cursor값:{cursor}')
        print(f'현재sentence값:{"".join(sentence_list)}')
    elif cmd == 'D':
        cursor +=1
        if cursor >len(sentence):
            cursor = len(sentence)
        print(f'현재cursor값:{cursor}')
        print(f'현재sentence값:{"".join(sentence_list)}')
    elif cmd == 'B':
        if cursor > 0:
            del sentence_list[cursor - 1]
            cursor -= 1
        print(f'현재cursor값:{cursor}')
        print(f'현재sentence값:{"".join(sentence_list)}')
    elif cmd =='P':
        sentence_list.insert(cursor, word)
        print(f'현재cursor값:{cursor}')
        print(f'현재sentence값:{"".join(sentence_list)}')
result=''.join(sentence_list)

print(result)
