# This script will generate a two coulmn data file  coprise of 1 - 10 in 1 columd and twice that in another column
echo 'xaxis yaxis' > data/linear_data.dat

#lets make a loop in order to make a column
for xdat in {1..10};
do
    echo $xdat  $((xdat*2)) >> data/linear_data.dat
done

echo blah blahX