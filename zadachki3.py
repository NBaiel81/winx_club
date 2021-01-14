# 17. У Софии был очень напряженный месяц и она решила взять отпуск на неделю.
# Чтобы избежать стресса во время отпуска, она хочет перенаправлять
# Стивену электронные письма со стрессовыми темами. Программа должна распознавать является ли
# тема письма стрессовой. Стрессовая тема определяется тем, что все буквы в верхнем
# регистре, и / или заканчиваются как минимум тремя восклицательными знаками,
# и / или содержат по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent".
# Список писем, которые пришли Sophie на почту, нужно отсортировать письма.
# По работе- которые содержат 'help','sos','urgent', рассылка из магазинов - начинается с
# 'sales', 'buy right now' внутри письма, такие письма относятся к спаму и их нужно записать в файл
# spam.txt, остальные записать в mail.txt
str1=['hello sophie how are you','hello pls help me!!!',
         'Sophie, production is dows go to work!!!',
         'sophie, i need your help',
         'SOS!!! come to work pls',
         'good night, Sophie',
         'SALES !Lining lala',
         'Nikes China Buy right now',
         'HeLP Sophie',
         'Hey sophie how are you',
         'Please come with me'
         ]
def sort_mails(mails_list:list):
    file1=open('spam.txt','a')
    file2=open('mail.txt','a')

    for i in mails_list:
        i=i.lower()
        str21 = i.endswith("!!!")


        if "help" in i or "asap" in i or "urgent" in i or "sos" in i:
            file1.write(i+"\n")
        elif "sales" in i or 'buy right now' in i or str21:
            file1.write(i+"\n")
        else:
            file2.write(i + "\n")



sort_mails(str1)

