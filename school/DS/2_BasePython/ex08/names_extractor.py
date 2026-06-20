import sys

def logic():
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as input, open("employees.tsv", "w", encoding="utf-8") as output:
            output.write("Name\tSurname\tE-mail\n")

            for line in input:
                email = line.strip()
                if not email:
                    continue
                fio = email.split('@' , 1)[0]
                name, surname = fio.split('.')
                output.write(f"{name.capitalize()}\t{surname.capitalize()}\t{email}\n")
    else:
        raise Exception("pass 1 filename")

if __name__ == "__main__":
    try:
        logic()
    except Exception as e:
        print(f"something is wrong : {e}")