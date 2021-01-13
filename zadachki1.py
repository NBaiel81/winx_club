# #append repieted number in l1 to l2 by one times each
# list1=[1,2,1,1,2,3,3,3,3,4,4,4,4,4]ist
# list2=[]
# for number in list1:
#     if number not in list2:
#         list2.append(number)
# print(list2)

#output should be 1st is number which repeated max times and 2nd is how many times
# list1=[1,2,2,3,3,3,4,4]
# 1st way
# list2=[]
# for i in list1:
#     list2.append(list1.count(i))
# max_count=max(list2)
# max_index=list2.index(max_count)
# result=list1[max_index]
# print(result,max_index)
# 2nd way
# dict1={}
# for i in list1:
#     dict1[i]=list1.count(i)
# print(dict1)
#
# # 2nd way to open file
# with open('hello.txt',"w") as f1:
#     # f1=open('hello.txt','w')
#     f1=open('hello.txt','w')
#     f1.write('hello ')
#     f1.write('hello')


