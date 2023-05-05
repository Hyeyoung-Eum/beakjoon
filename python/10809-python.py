S = input()
alphabet = list(range(97, 123))
for _ in alphabet:
    print(S.find(chr(_)), end=' ')        