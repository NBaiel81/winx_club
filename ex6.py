# 6.	Акылбек решил поехать в горы. Начал собирать провизию в дорогу, как оказалось места
# недостаточно, Акылбек решил найти продукт с самым большим количеством (больше всех повторяется).
# Всю еду Акылбек записал в список. Напишите функцию, которая принимает список еды, как аргумент.
#+ удалить result from item_list
# item_list=['p','p','p','p','o','o','o','l','l','i']
def backpack(item_list:list):
    i=0
    list2=[]
    while i<len(item_list):
        item_count=item_list.count(item_list[i])
        list2.append(item_count)
        i+=1
    max_list=max(list2)
    result_elem=item_list[list2.index(max_list)]
    j=0
    while j<max_list:
        item_list.remove(result_elem)
        j+= 1
    return result_elem, max_list,item_list
a=backpack(['p','p','p','p','o','o','o','l','l','i'])
print(a)


