import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + rgb[j][2]
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])

print(ans)