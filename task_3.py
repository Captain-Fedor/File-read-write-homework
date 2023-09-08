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
def writing_file(file: str, length: int):
    with codecs.open('final_task_3.txt', 'a', encoding='utf-8') as data:
        file +='\n'
        data.write(file)
        data.write(str(length)+'\n')
#     with codecs.open(file, encoding='utf-8', 'r'):
#     with codecs.open('final_task_3.txt',encoding='utf-8', 'a'):
# #         ...
writing_file('45.txt', 5)
# for file_data in sort_dict:



