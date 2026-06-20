def parse_csv_line(line):
    values = []
    current_value = ""
    inside_quotes = False

    for char in line.strip():
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ',' and not inside_quotes:
            values.append(current_value)
            current_value = ""
        else:
            current_value += char

    values.append(current_value)
    return values

def parse_file():
    input_file_path = "ds.csv"
    output_file_path = "ds.tsv"
    with open(input_file_path, 'r', encoding='utf-8') as csv_in, \
        open(output_file_path, 'w', encoding='utf-8') as tsv_out:

        for line in csv_in:
            parsed_values = parse_csv_line(line)
            tsv_out.write("\t".join(parsed_values) + "\n")

if __name__ == "__main__":
    parse_file()