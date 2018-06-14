#!/bin/python
from itertools import combinations
from collections import Counter
import sys


def countSubs(s):
    # Complete this function
    s_list = list(s)
    s_len = len(s)

    ans = 0
    for i in xrange(2, s_len):

        subs = list(combinations(s_list, i))

        for elem in subs:
            subs_counter = Counter(elem)

            if len(subs_counter.keys()) % 2 == 0:
                check1, check2 = True, True

                if 'a' in subs_counter.keys():
                    if 'b' in subs_counter.keys():
                        if subs_counter['a'] != subs_counter['b']:
                            check1 = False
                    else:
                        check1 = False

                if 'c' in subs_counter.keys():
                    if 'd' in subs_counter.keys():
                        if subs_counter['c'] != subs_counter['d']:
                            check2 = False
                    else:
                        check2 = False

                if check1 and check2:
                    ans += 1

    return ans

# Return the number of non-empty perfect subsequences mod 1000000007
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = countSubs(s)
    print(result)



