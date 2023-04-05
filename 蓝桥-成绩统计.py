import os
import sys

n = int(input())
good = pas = 0
for i in range(n):
    score = int(input())
    if score >= 85:
        good += 1
    if score >= 60:
        pas += 1
print('%.0f%%' % (float(pas/n)*100))
print('%.0f%%' % (float(good/n)*100))
