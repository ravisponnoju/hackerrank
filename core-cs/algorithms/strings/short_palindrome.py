
def count_of_palindrome_sub_seqs(s):
    N = len(s)

    temp = [0] * N
    s_pal_2D = []
    for i in xrange(N):
        s_pal_2D.append(list(temp))

    for i in xrange(N):
        s_pal_2D[i][i] = 1

    for L in xrange(2, N + 1):

        for i in xrange(N - L):
            k = L + i - 1

            if s[i] == s[k]:
                s_pal_2D[i][k] = s_pal_2D[i][k - 1] + s_pal_2D[i + 1][k] + 1
            else:
                s_pal_2D[i][k] = s_pal_2D[i][k - 1] + s_pal_2D[i + 1][k] - s_pal_2D[i + 1][k - 1]

    print s_pal_2D
    return s_pal_2D[0][N - 1]

s = raw_input().strip()
print count_of_palindrome_sub_seqs(s)
