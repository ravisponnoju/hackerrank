
def identify_paths_with_max_cost():
    global edges
    global lengths

    ans = {}

    for i in xrange(1, max(lengths.keys()) + 1):
        edg = lengths[i]

        for ed in edg:
            u, v = ed[0], ed[1]

            ver_attached = edges[u]

            for ver in ver_attached:
                if 

    return ans

N, Q = map(int, raw_input().strip().split(' '))

edges = {}
lengths = {}
# answer = {}
for e in xrange(N - 1):
    u, v, l = map(int, raw_input().strip().split(' '))

    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    # try:
        # edges[v].append(u)
    # except KeyError:
        # edges[v] = [u]

    try:
        lengths[l].extend([(u, v)])
    except KeyError:
        lengths[l] = [(u, v)]


answer = identify_paths_with_max_cost()

print answer
