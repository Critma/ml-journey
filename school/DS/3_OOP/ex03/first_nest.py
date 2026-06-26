import sys, os

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self, has_reader = True) -> list[list]:
        result = []
        with open(self.file_name, 'r', encoding='utf-8') as file:
            first = has_reader
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
                result.append([int(x) for x in tmp])
        return result

    class Calculations:
        def counts(list: list[list]) -> tuple[int, int]:
            heads, tails = 0, 0
            for values in list:
                if values[0] == 1 and values[1] == 0:
                    heads += 1
                elif values[0] == 0 and values[1] == 1:
                    tails += 1
                else:
                    raise Exception("counts: values is invalid", values)
            return heads, tails
                
        def fractions(values: tuple[int, int]) -> tuple[float, float]:
            sum = values[0] + values[1]
            return round(values[0] / sum, 4), round(values[1] / sum, 4)

if __name__ == '__main__':
    try:
        research = Research('../data/'+ sys.argv[1])
        data = research.file_reader()
        print(data)
        heads_tails = research.Calculations.counts(data)
        print(*heads_tails)
        print(*research.Calculations.fractions(heads_tails))
    except Exception as e:
        print('exception:',e)
    