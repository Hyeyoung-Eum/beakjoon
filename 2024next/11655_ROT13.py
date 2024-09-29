import sys

def input():
    return sys.stdin.readline().rstrip()

def rot13(s):
    result = []  # 결과를 저장할 리스트

    for char in s:
        # 대문자 변환
        if 'A' <= char <= 'Z':
            # 대문자는 'A'를 기준으로 13글자씩 밀어서 변환
            new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(new_char)
        # 소문자 변환
        elif 'a' <= char <= 'z':
            # 소문자는 'a'를 기준으로 13글자씩 밀어서 변환
            new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 알파벳이 아닌 문자는 그대로 유지
            result.append(char)

    return ''.join(result)

s = input()

encrypted_s = rot13(s)

print(encrypted_s)
