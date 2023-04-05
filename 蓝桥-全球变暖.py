import os
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

vis=[[0]*n for i in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = True
q = []


def bfs(x, y):
    global flag
    q.append((x, y))
    vis[x][y] = 1
    while len(q):
        item = q.pop(0)
        tx, ty = item[0], item[1]
        if arr[tx][ty + 1] == '#' and arr[tx][ty - 1] == '#' and arr[tx - 1][ty] == '#' and arr[tx + 1][ty] == '#':
            flag = False
        for i in range(4):
            nx = tx + dir[i][0]
            ny = ty + dir[i][1]
            if vis[nx][ny] == 0 and arr[nx][ny] == '#':
                q.append((nx, ny))
                vis[nx][ny] = 1


ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#' and vis[i][j] == 0:
            flag = True
            bfs(i, j)
            if flag:
                ans += 1
print(ans)