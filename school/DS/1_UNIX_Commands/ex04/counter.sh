file=../ex03/hh_positions.csv

title="\"name\",\"count\""

content=$(tail -n +2 $file)
content=$(echo "$content" | awk -F, '{print $3}' | sort | uniq -c | sort -r | awk 'BEGIN{OFS=","} {print $2, $1}')
# remove "-"
# content=$(echo "$content" | awk -F, '{print $3}' | sort | uniq -c | sort -r | awk 'BEGIN{OFS=","} {print $2, $1}' | grep -v '^"-\"') 

echo -e "$title\n$content" > hh_uniq_positions.csv