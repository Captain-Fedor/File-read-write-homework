
import codecs
def writing_file(file: str, length: int):
    print(file)
    file_read = file
    with codecs.open('final_task_3.txt', 'a', encoding='utf-8') as data:
        file +='\n'
        data.write(file)
        data.write(str(length)+'\n')
    with codecs.open(file_read, 'r', encoding='utf-8') as data:
        f = data.readlines()
    return f

    # with open(file) as data:
    #     file_read_list = data.readlines()
    # return print(file_read_list)

print(writing_file('1.txt', 6))
