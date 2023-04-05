import os
import sys

# 请在此输入您的代码
n,m=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
for i in range(m):
  u,v=list(map(int,input().split()))
  graph[u].append(v)
  graph[v].append(u)
cnt=0
for k in range(1,n+1):
  for i in graph[k]:
    for j in graph[i]:
      if j!=k:
        cnt+=(len(graph[j])-1)
print(cnt)