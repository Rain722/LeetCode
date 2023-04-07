import os
import sys

# 记忆化搜搜写法
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    res = 1
    for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dirx
        ny = y + diry
        if 0 <= nx <n and  0 <= ny < m and arr[x][y] > arr[nx][ny]:
            res = max(dfs(nx, ny)+1, res)
    dp[x][y] = res
    return res

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dfs(i, j))
print(ans)
