# 7.	Айгерим решила написать игру для детского сада, дети будут угадывать
# число, дается 5 попыток, при неудачной попытке, прогр
# амма отвечает тем, что если введенное ребенком числ
# о больше загаданного, выводится знак “>”, меньше “<”, когда ребенок угадывает
# число, программа поздравляет.
# В этой задаче нужно использовать random, сначала нужно импортировать.
# Напишите функцию которая генерирует случайное число и дает возможность ввода в  консоль, числа.

def game():
    import random
    rand_number=random.randint(0,10)
    tries=0
    while tries<5:
        tries+=1
        kid_guess=int(input())
        if kid_guess<rand_number and tries<=4:
            print("<")
        elif kid_guess>rand_number and tries<=4:
            print(">")
        elif kid_guess==rand_number and tries<=4:
            print("Congratulation!!!")
            break
    if tries==5:
        print("fail")
game()
#




