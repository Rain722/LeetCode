import os
import sys

s = list(input())
m = sorted(sorted(s), key=lambda x:s.count(x), reverse=True)[0]
print(m, s.count(m), sep='\n')