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


