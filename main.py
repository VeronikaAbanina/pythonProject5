import os

ROOT_PATH = os.getcwd()
FILE_DIR = 'logs'
directory = '/Users/veronika/PycharmProjects/pythonProject5/logs'
files = os.listdir(directory)
file_dict = {}

for file in files:
    file_path = os.path.join(ROOT_PATH, FILE_DIR, file)
    with open(file_path) as files_to_read:
        text = []
        for strings in files_to_read:
            text.append(strings.strip())
            lens = len(text)
            file_dict[file] = [len(text), text]

sorted_list = sorted(file_dict.items(), key=lambda item: item[1])
with open('total', 'w') as files_to_write:
    for files_ in sorted_list:
        files_to_write.write(f'{files_ [0]}\n')
        files_to_write.write(f'{files_ [1][0]}\n')
        for text_ in files_[1][1]:
            line = ''.join(str(x) for x in text_)
            files_to_write.write(f'{line}\n')