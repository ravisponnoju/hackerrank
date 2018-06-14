
def minimumPasses(m, w, p, n):
    # Complete this function
    if m * w >= n:
        return 1

    ans = 0
    big, small = max(m, w), min(m, w)
    prod = big * small

    while prod < n:
        buy_capacity = prod / p

        if buy_capacity <= big - small:
            small += buy_capacity
        else:
            buy_capacity -= big - small
            small = big

            if buy_capacity & 1:
                small_part = buy_capacity / 2
                big_part = buy_capacity - small_part

                big += big_part
                small += small_part

            else:
                each_part = buy_capacity / 2

                big += each_part
                small += each_part

        prod = big * small
        ans += 1

    print big, small
    return ans

if __name__ == "__main__":
    m, w, p, n = raw_input().strip().split(' ')
    m, w, p, n = [long(m), long(w), long(p), long(n)]
    result = minimumPasses(m, w, p, n)
    print result
