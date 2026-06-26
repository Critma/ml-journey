import sys
from random import randint
import logging

def LoggingInit():
    logging.basicConfig(
    filename='analytics.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='w')


class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self, has_reader = True) -> list[list]:
        logging.info('Reading a file'+ self.file_name)
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
        def __init__(self, data: list[list]):
            self.data = data

        def counts(self) -> tuple[int, int]:
            logging.info('Calculating the counts of heads and tails')
            heads, tails = 0, 0
            for values in self.data:
                if values[0] == 1 and values[1] == 0:
                    heads += 1
                elif values[0] == 0 and values[1] == 1:
                    tails += 1
                else:
                    raise Exception("counts: values is invalid", values)
            return heads, tails
                
        def fractions(self, values: tuple[int, int]) -> tuple[float, float]:
            logging.info('Calculating the fractions of heads and tails')
            sum = values[0] + values[1]
            return round(values[0] / sum, 4), round(values[1] / sum, 4)

class Analytics(Research.Calculations):
    def predict_random(self, amount: int) -> list[list]:
        logging.info('Predicting the heads and tails')
        result = []
        for _ in range(amount):
            rnd = randint(0, 1)
            result.append([rnd, 1 - rnd])
        return result

    def predict_last(self) -> list:
        logging.info('Predicting the last element')
        return self.data[-1]

    def get_report(self, template:str, forecast:list[list]) -> str:
        logging.info('Generate a report')
        heads, tails = self.counts()
        heads_prob, tails_prob = self.fractions((heads, tails))
        forecast_heads, forecast_tails = Analytics(forecast).counts()
        return template.format(observation_count=len(self.data), tails=tails, heads=heads, tails_prob=tails_prob*100, heads_prob=heads_prob*100, forecast=len(forecast), forecast_heads=forecast_heads, forecast_tails=forecast_tails)

    def save_file(self, data: any, file_name:str, extension='txt'):
        logging.info('Saving a report')
        file_path = f"{file_name}.{extension}"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
