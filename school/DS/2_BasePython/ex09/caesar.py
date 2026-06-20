import sys

def caesar_shift(line: str, shift: int) -> str:
    if contains_cyrillic(line):
        raise Exception("The script does not support your language yet.")
    result = ''
    for char in line:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def contains_cyrillic(text):
    # A - я
    return any(1040 <= ord(ch) <= 1103 or ch == 'ё' or ch == 'Ё' for ch in text)


def logic():
    if len(sys.argv) != 4:
        raise Exception("pass {command 'message' count_to_shift}")

    match sys.argv[1]:
        case "encode":
            print(caesar_shift(sys.argv[2], int(sys.argv[3])))
        case "decode":
            print(caesar_shift(sys.argv[2], -int(sys.argv[3])))
        case _:
            raise Exception("unknown command")

if __name__ == "__main__":
    try:
        logic()
    except Exception as e:
        print(f"something is wrong : {e}")