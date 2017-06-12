read count
# echo $count
total=0
for i in `seq 1 $count`;
do
    read value
    total=`echo "$total + $value" | bc -l`
done
# echo $total
printf "%.3f" `echo "$total / $count" | bc -l`