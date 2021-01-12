string1="hello hello world"
print(string1.split())#devide into separate elem between acording to probel
print(string1.index(' '))#show index of ' ' and .find the same but if didnt find letter shows -1
print(string1.strip())#removes probel in the begining and end of the text
string2=string1.replace('hello','Hi',1)#1st value-what will be replaced,2nd to what will be replaced, 3rd how many of 1st value will be replaced
print(string2)
print(string1.startswith('o'))#checking whether str starts from o and also .endswith
print(string1.upper())# makes all in upper register also .title only 1st letter, also islower which check then true false
print(string1.capitalize())#turn only 1st letter into upper register
print(string1.isalnum())#check if str include only num or letters, .isalpha only num
print(string1[2:3])# from 2nd letter to 3rd

