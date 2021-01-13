# if in str1 only 'a' True,else False
str1='aaaaaaa'
# list1=str1.split()
# print(str1,list1)
# list1.remove(max(list1))
# print(str1,list1)
b=0
for i in str1:
    if i=="a":
        b+=1
if b==len(str1):
    print(True)
else:
    print(False)

