import sys
input=sys.stdin.readline

#DP를 써야할 것 같다.
def find_combinations(n, k):
    def backtrack(remaining_sum, k, start, path, result):
        if k == 0:
            if remaining_sum == 0:
                result.append(path[:])
            return
        for i in range(start, n + 1):
            if remaining_sum - i >= 0:
                path.append(i)
                backtrack(remaining_sum - i, k - 1, 0, path, result)  # 0부터 시작해서 중복 허용
                path.pop()

    result = []
    backtrack(n, k, 0, [], result)
    return result

combinations = find_combinations(N, K)

N=int(input())
#P[1]부터 들어올 수 있도록, 앞에 0추가.
P_list=[0]+list(map(int,input().split()))
