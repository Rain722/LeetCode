h = int(input())  # 输入数据
W = [list(map(int, input().split())) for i in range(h)]
# 循环遍历计算到每一行的和的最大值
for i in range(1, h):
    for j in range(0, i + 1):
        if j == 0:  # 最左边元素只能由右上方得到
            W[i][j] += W[i - 1][j]
        elif j == i:  # 最右边元素只能由左上方得到
            W[i][j] += W[i - 1][j - 1]
        else:  # 其余元素由上方较大值得到
            W[i][j] += max(W[i - 1][j - 1: j + 1])
if h & 1:  # 如果是奇数行，则返回最中间值
    print(W[-1][h // 2])
else:  # 偶数行则返回中间较大值
    print(max(W[-1][h // 2 - 1], W[-1][h // 2]))