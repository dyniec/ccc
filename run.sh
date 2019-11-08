mkdir out
for i in $(ls in);
do
	echo running on $i;
	$* <in/$i >out/$i.out 
done
