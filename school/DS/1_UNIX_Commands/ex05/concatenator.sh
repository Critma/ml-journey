#!/bin/bash

OUTPUT_FILE="combined_hh_positions.csv"

if [ $# -eq 0 ]; then
    echo "Error: No input files specified."
    echo "Use: ./concatenator.sh *.csv"
    exit 1
fi

rm -f "$OUTPUT_FILE"

is_first_file=true

for file in "$@"; do
    # Check if the current item is a regular file (not a directory)
    if [ -f "$file" ]; then
        if $is_first_file; then
            cp "$file" "$OUTPUT_FILE"
            is_first_file=false
            echo "Header and data from '$file' have been written."
        else
            # append only the data to the existing output file.
            tail -n +2 "$file" >> "$OUTPUT_FILE"
            echo "Data from '$file' has been appended."
        fi
    else
        echo "Warning: Skipping '$file'. It is not a valid file."
    fi
done

# sort
title=$(cat $OUTPUT_FILE | head -n 1)
sorted=$(cat $OUTPUT_FILE | tail -n +2 | sort -t ',' -k2r -k1)
echo -e "$title\n$sorted" > $OUTPUT_FILE

echo "Concatenation complete. Final result saved in '$OUTPUT_FILE'"