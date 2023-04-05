import os
import sys

from itertools import *
n = int(input())
s = input().split()
lst = list()
for item in permutations(s):
    a = ''.join(item)
    lst.append(int(a))
print(max(lst))
