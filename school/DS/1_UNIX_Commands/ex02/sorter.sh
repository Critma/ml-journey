title=$(cat ../ex01/hh.csv | head -n 1)
sorted=$(cat ../ex01/hh.csv | tail -n +2 | sort -t ',' -k2r -k1)
echo -e "$title\n$sorted" > hh_sorted.csv