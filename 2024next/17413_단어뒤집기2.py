def reverse_words_in_string(s):
    result = []  # 최종 결과를 저장할 리스트
    word = []  # 현재 단어를 저장할 리스트
    inside_tag = False  # 현재 태그 내부인지 여부를 나타내는 플래그

    for char in s:
        if char == '<':
            # 태그의 시작을 만났을 때
            # 현재 word 리스트를 뒤집어 result에 추가하고 word를 초기화
            if word:
                result.extend(word[::-1])
                word = []
            # 태그 내부로 진입했으므로 inside_tag를 True로 설정
            inside_tag = True
            # '<'를 result에 추가
            result.append(char)
        elif char == '>':
            # 태그의 끝을 만났을 때
            # 태그 내부가 끝났으므로 inside_tag를 False로 설정
            inside_tag = False
            # '>'를 result에 추가
            result.append(char)
        elif inside_tag:
            # 태그 내부에 있는 문자를 만났을 때
            # 그대로 result에 추가
            result.append(char)
        elif char == ' ':
            # 공백 문자를 만났을 때 (단어의 끝)
            # 현재 word 리스트를 뒤집어 result에 추가하고 word를 초기화
            result.extend(word[::-1])
            result.append(char)
            word = []
        else:
            # 일반 문자를 만났을 때
            # 현재 단어(word)에 추가
            word.append(char)

    # 마지막 단어가 남아 있을 수 있으므로 이를 처리
    if word:
        result.extend(word[::-1])

    # result 리스트를 문자열로 변환하여 반환
    return ''.join(result)

# 입력받기
s = input().strip()
print(reverse_words_in_string(s))
