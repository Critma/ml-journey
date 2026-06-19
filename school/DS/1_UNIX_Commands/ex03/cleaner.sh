file=../ex02/hh_sorted.csv

gawk -F, '
BEGIN {
    OFS = ","
}
# skip header
NR == 1 {
    print;
    next;
}
{
    FPAT = "([^,]+)|(\"[^\"]+\")"

    levels = ""
    while (match($3, /(Junior|Middle|Senior)/)) {
        if (levels != "") levels = levels "/"
        levels = levels substr($3, RSTART, RLENGTH)
        $3 = substr($3, RSTART + RLENGTH)
    }
    
    $3 = (levels != "" ? levels : "-")
    $3 = "\"" $3 "\""

    print
}' "$file" > hh_positions.csv