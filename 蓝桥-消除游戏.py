import os
import sys

li = list(input())
stop = 0

while stop < 2**64:
    pos = set()
    for i in range(1, len(li)-1):
        if li[i] == li[i+1] and li[i-1] != li[i]:
            pos.add(i)
            pos.add(i-1)
        if li[i] == li[i-1] and li[i] != li[i+1]:
            pos.add(i)
            pos.add(i+1)
    if len(pos) == 0:
        print("".join(li))
        break
    li1 = []
    for t in range(len(li)):
        if t not in pos:
            li1.append(li[t])
    li = li1.copy()
    pos.clear()
    if len(li) == 0:
        print("EMPTY")
        break
    stop += 1