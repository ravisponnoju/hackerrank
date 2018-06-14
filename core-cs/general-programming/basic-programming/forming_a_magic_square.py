

inp_arr = []
for i in xrange(3):
    inp_arr.append(map(int, raw_input().strip().split(' ')))

sum_row = []
sum_col = []
for i in xrange(3):
    sum_temp1 = 0
    sum_temp2 = 0
    for j in xrange(3):
        sum_temp1 += inp_arr[i][j]
        sum_temp2 += inp_arr[j][i]
    sum_row.append(sum_temp1)
    sum_col.append(sum_temp2)

sum_dgn = [inp_arr[0][0] + inp_arr[1][1] + inp_arr[2][2], \
           inp_arr[0][2] + inp_arr[1][1] + inp_arr[2][0]]

print sum_row, sum_col, sum_dgn

