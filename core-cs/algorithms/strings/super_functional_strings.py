from collections import Counter
import timeit

start = timeit.default_timer()

T = int(raw_input().strip())


for t in xrange(T):
    s = raw_input().strip()
    s_list = list(s)

    F = 0
    string_hash = set([])
    # print s_list

    for i in xrange(len(s)):
        for j in xrange(i, len(s)):
            string = ''.join(s_list[i:j + 1])

            if string not in string_hash:
                string_hash.add(string)
                string_counter = Counter(string)
                # print string, string_counter

                F += len(string) ** len(string_counter.keys())

    print F

print timeit.default_timer() - start
