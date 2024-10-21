from itertools import combinations

n,m = map(int, input().split())
numbers= list(map(int, input().split()))

numbers.sort()

for comb in combinations(numbers, m):
    print(comb[0], comb[1])

