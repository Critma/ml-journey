import sys, os

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self) -> str:
        result = ''
        with open(self.file_name, 'r', encoding='utf-8') as file:
            first = True
            for line in file:
                tmp = list(map(lambda x: x.strip(), line.split(',')))
                if len(tmp) != 2:
                        raise Exception('not 2 strings')
                if first:
                    first = not first
                    continue
                else:
                    if  tmp[0] == tmp[1]:
                        raise Exception('same strings')
                    if '0' not in tmp or '1' not in tmp:
                        raise Exception('values is not 1 or 0')
                result += line
        return result

if __name__ == '__main__':
    try:
        print(Research('../data/'+sys.argv[1]).file_reader())
    except Exception as e:
        print('exception:', e)
    