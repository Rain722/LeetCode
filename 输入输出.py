# 一维数组
# arr = input(" ")
# num = [int(n) for n in arr.split()]
# print(num)

# 二维整形数组
n, m = map(int, input().split())
# 列表式生成法
# arr = [[0 for i in range(m)] for j in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(" "))))

for i in range(n):
    for j in range(m):
        print('%d' % arr[i][j], end=' ' if j!=(m-1) else '')
    print("")