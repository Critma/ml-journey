#!/bin/bash

rm -f *.csv

INPUT_DELIMITER=","
DATE_COLUMN=2
SKIP_HEADER=true

# stdin check
if [ -t 0 ]; then
    echo "Erorr: This script consume stdin."
    echo "Use: cat ../ex03/hh_positions.csv | ./partitioner.sh"
    exit 1
fi

while IFS=$'\n' read -r line; do
    if $SKIP_HEADER && [ -z "$header" ]; then
        header="$line"
        continue
    fi

    date_full=$(echo "$line" | awk -F"$INPUT_DELIMITER" '{print $'$DATE_COLUMN'}')
    date_day=$(echo "$date_full" | awk -FT '{print $1}')
    date_day=$(echo $date_day | cut -c1 --complement)

    output_file="${date_day}.csv"

    # write header
    if [ ! -f "$output_file" ]; then
        if $SKIP_HEADER; then
            echo "$header" > "$output_file"
        fi
    fi

    echo "$line" >> "$output_file"
done