import codecs

file_list = ['1.txt', '2.txt', '3.txt']
sort_dict = {}

def count_file_lines(file:str):
    with codecs.open(file, encoding='utf-8') as data:
        length = len(data.readlines())
        # sort_dict[file] = length
    return length

for file_name in file_list:
    sort_dict[file_name] = count_file_lines(file_name)

sort_dict = sorted(sort_dict.items(), key = lambda x: x[1])
print(sort_dict)

def writing_file(file: str, length: int): # запись в финальный файл выбранного файла
    print(file)
    # print(f"'{file}'")
    with codecs.open('final_task_3.txt', 'a', encoding='utf-8') as data:
        file +='\n'
        data.write(file)
        file = file.strip()
        data.write(str(length)+'\n')

    with codecs.open(file, 'r', encoding='utf-8') as data:
        file_list = data.readlines()
        file_list[-1] = file_list[-1] + '\r\n'
        print(file_list)
        print(file_list[-1])
    with codecs.open('final_task_3.txt', 'a', encoding='utf-8') as data:
        for line in file_list:
            data.write(line)

for file in sort_dict:
    writing_file(file[0], file[1])



#     with codecs.open(file, encoding='utf-8', 'r'):
#     with codecs.open('final_task_3.txt',encoding='utf-8', 'a'):
# #         ...
# for file in sort_dict:

# for file_data in sort_dict:



