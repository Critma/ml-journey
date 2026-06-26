class Must_Read:
    file_name = '../data/data.csv'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())
    except Exception as e:
        print(e)

if __name__ == '__main__':
    Must_Read()