# 3.	Напишите функцию принимающая параметр x, которая
# выведет True если х находится в списке и False в противоположном случае.
list1=[1,2,3,4,5,6,7,8]
x=int(input())
def baiel(x):
    i=0
    while i<len(list1):
        if x==list1[i]:
            True
            print(True)
        else:
            False
            print(False)
        i+=1
baiel(x)

