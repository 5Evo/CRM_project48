from pathlib import Path

def read_data(file):
    dir_name = 'project48/test_data/'
    path_to_file = Path.cwd() / dir_name / file
    try:
        with open(path_to_file, 'r') as f:
            result = f.read().split("\n")
    except Exception as e:
        print(f'Не смогли прочитать файл {file}. Ошибка: {e}')
        result = []
    return result


if __name__ == '__main__':

    files = ['status.txt', 'action.txt']
    for file in files:
        data_from_file = read_data(file)
        print(f'------------- Прочитали {file}-----------')
        for item in data_from_file:
            print(item)