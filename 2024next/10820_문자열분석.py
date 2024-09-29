import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    try:
        string = input()
        answer = [0] * 4
        for s in string:
            if s.islower():
                answer[0] += 1
            elif s.isupper():
                answer[1] += 1
            elif s.isdigit():
                answer[2] += 1
            elif s == ' ':
                answer[3] += 1
        print(*answer)
    except EOFError:
        break