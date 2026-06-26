class Research:
    def file_reader() -> str:
        file_name = '../data/data.csv'
        with open(file_name, 'r', encoding='utf-8') as file:
                return file.read()

if __name__ == '__main__':
    try:
        print(Research.file_reader())
    except Exception as e:
        print(e)