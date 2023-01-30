def f(s, t):
    S = [0]
    S_Up = []
    T = [0]
    T_Up = []
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            S_Up.append(i)
    S_Up.append(len(s))

    for i in range(len(t)):
        if 'A' <= t[i] <= 'Z':
            T_Up.append(i)
    T_Up.append(len(t))

    for i in range(len(S_Up) - 1):
        l = S_Up[i]
        r = S_Up[i + 1]
        S.append(s[l:r])

    for i in range(len(T_Up) - 1):
        l = T_Up[i]
        r = T_Up[i + 1]
        T.append(t[l:r])

    n = len(S)
    m = len(T)
    dp = [[0 for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if S[i] == T[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[n - 1][m - 1])


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    f(s, t)
