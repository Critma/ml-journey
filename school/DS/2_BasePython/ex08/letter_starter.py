import sys

def logic():
    if len(sys.argv) == 2:
        with open("employees.tsv", "r", encoding="utf-8") as input:
            for line in input:
                if sys.argv[1] not in line:
                    continue
                name = line.split("\t")[0]
                print(f"Dear {name}, welcome to our team! \
We are sure that it will be a pleasure to work with you.\
That’s a precondition for the professionals that our company hires.")
    else:
        raise Exception("pass 1 e-mail")

if __name__ == "__main__":
    try:
        logic()
    except Exception as e:
        print(f"something is wrong : {e}")