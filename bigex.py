# Нужно написать функцию регистрации, которая содержит в себе код (целое число) и обычный механизм авторизации.
# Затем написать функцию, которая принимает в параметрах только код и сверяет с тем что ранее был отправлен.
# Дан список товаров разных категорий: Телефоны, Компьютеры, видеокарты и жесткие диски. Нужно создать функцию,
# которая записывает все товары в файл, для дальнейших работ. Нужно создать функцию, которая считывает из файла все строки
# и сортирует по отдельным файлам категорий: например все что касается телефонов в файле с телефонами. Далее нужно написать функцию,
# которая будет открывать файл указанный в параметрах. Последний шаг – пользователь вводит как он хочет отфильтровать товары:
# например, ‘phones’ – вывести все строки из файла с телефонами.

def regist(name,password,check_password):
    list1=[]
    if len(name)<8 and len(password)<8 and password==check_password:
        list1.append(name)
        list1.append(password)
    return list1
result=regist('Baiel','1234','1234')
name1=result[0]
password1=result[1]

def avtor():
    i=0
    while i<=3:
        check_name=input()
        check_password1=input()
        check_password2=input()
        i+=1
        if check_name==name1 and check_password1==password1 and check_password1==check_password2:
            print("ok")
        else:
            print('not ok')
text=['burger1','burger2','burger3','dress1','dress2', 'dress3', 'comp1', 'comp2', 'comp3', 'item1', 'item2', 'item3', 'book1', 'book2', 'book3']
def write_to(filename,text):
    file=open(filename,'a')
    file.write(text+'\n')
for line in text:
    write_to('test1', line)

def sort_file():
    for product in text:
        if 'burger1' in product or "burger2" in product or 'burger3' in product:
            write_to('food',product)
        elif 'dress1' in product or "dress2" in product or 'dress3' in product:
            write_to('clothes', product)
        elif 'comp1' in product or 'comp2' in product or 'comp3' in product:
            write_to('electronic',product)
        elif 'item1' in product or 'item2' in product or 'item3' in product:
            write_to('items',product)
        elif 'book1' in product or 'book2' in product or 'book3' in product:
            write_to('books',product)
sort_file()

def open_file():
    ask_file=input()
    if ask_file=="food":
        file1=open('food','r')
        print(file1.read())
    elif ask_file=="clothes":
        file1 = open('clothes')
        print(file1.read())
    elif ask_file=="electronic":
        file1 = open('electronic','r')
        print(file1.read())
    elif ask_file=="items":
        file1 = open('items','r')
        print(file1.read())
    elif ask_file=="books":
        file1 = open('books','r')
        print(file1.read())
open_file()

















