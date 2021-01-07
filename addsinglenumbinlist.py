list1=[1,2,3,3,3,4,4,4,5,5,6,6]
list2=[]
i=0
while i < len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i+=1
print(list2)
# or print(set(list1))
# readlines divide into list acording to lines
# strip remove empty lines