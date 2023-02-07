n = int(input())
def PrimeFactor(n):
    res = dict()
    for i in [2,3]:
        while n != i:
            if n%i == 0:
                if i in res:
                    res[i] += 1
                else:
                    res[i] = 1
                n //= i
            else:
                break
    for j in range(1, int(n**0.5//6+2)):    # 开方有一次误差，除6又有一次误差，所以加2，保证至少进来一次
        i_1 = 6*j - 1   # 前几个的质数：2,3,5,7,11，13....发现除了2,3其他的都是6的整数倍加1或者减1（当然有例外），所以用6来作为基准   这是前面一个数
        i_2 = 6*j + 1   # 后面一个数
        for i in [i_1, i_2]:
            while n != i:
                if n % i == 0:
                    if i in res:
                        res[i] += 1
                    else:
                        res[i] = 1
                    n //= i
                else:
                    break
    res[n] = 1  # n本身就是一个质数
    return res

vis = PrimeFactor(n)
print(len(vis))