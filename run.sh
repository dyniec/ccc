mkdir -p in
mkdir -p out

for i in $(ls in);
do
	echo running on $i;
	$* <in/$i >out/$i.out 
done
