import codecs


with codecs.open('text_1.txt', encoding='utf-8') as data:
    length = len(data.readlines())

with codecs.open('text_1.txt', encoding='utf-8') as data:
    dish = []
    contents =[]
    for i in range(length):
        line = data.readline()
        if line == '\r\n':
            dish = list(map(lambda x: x.replace('|', ','), dish))
            contents.append(dish)
            dish = dish.copy()
            dish.clear()
        else:
            line = line.strip()
            dish.append(line)
    dish = list(map(lambda x: x.replace('|', ','), dish))
    contents.append(dish)

def make_ingrid_list(list): # словарь словарей из ингридиентов с названием блюда
    item_list = []
    item_dict = {}
    for item in list[2:]:
        item = item.split(',')
        item_list.append({'ingridient name': item[0], 'quantity': item[1], 'measure': item[2]})
    item_dict[list[0]] = item_list
    return item_dict

'''здача 1 формирование списка'''

cook_book = {}
for item in contents:
    cook_book.update(make_ingrid_list(item))

print(cook_book)
print()

'''задача 2 подсчет ингридиентов и количества от людей '''

man_count = 2
dishes = ['Запеченный картофель', 'Омлет']

shop_dict ={} #словарь с учетом количества персон

for key, item in cook_book.items():
    for ingridient in item:
        ingridient['quantity'] = int(ingridient['quantity']) * man_count


ingridient_list =[] #лист из ингридиентов с повторениями.
for dish in dishes:
    for key in cook_book.keys():
        if key == dish:
            ingridient_list +=(cook_book[dish])
            # ingridient_list.append(cook_book[dish])


shopping_dict = {} #отсеивание повторяющихся ингридиентов
for product in ingridient_list:
    if product['ingridient name'] in shopping_dict.keys():
        product['quantity'] += product['quantity']
        shopping_dict[product['ingridient name']] = {'measure': product['measure'], 'quantity': product['quantity']}
    else:
        shopping_dict[product['ingridient name']] = {'measure': product['measure'], 'quantity': product['quantity']}

print(shopping_dict)

