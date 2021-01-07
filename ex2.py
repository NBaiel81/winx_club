# 2.	Напишите функцию которая в аргументах принимает x и list1, удалите из с
# писка все элементы которые равны x.
list1=[1,2,3,4,5,6,7,8,9]

x=int(input())
def function(x,list1):
    i=0
    while i<len(list1):
        if list1[i]==x:
            list1.remove(list1[i])
        i+=1
    print(list1)
function(x,list1)