# Мишка Лимак хочет стать самым большим медведем, ну, или хотя бы стать больше своего старшего брата Боба.
# Сейчас вес Лимака равен a, а вес Боба равен b. Гарантируется, что вес Лимака меньше или равен весу Боба.
# Лимак ест много, и его вес утраивается каждый год, а вес Боба удваивается каждый год.
# Через сколько целых лет Лимак станет строго больше (т. е. будет весить строго больше) Боба?
number=list(map(int,input().split()))
limak=number[0]
bob=number[1]
1<=limak<=bob<=10
count_years=0
1<=limak<=bob<=10
if 1 <= limak <= bob <= 10:
    while limak<=bob:
        limak*=3
        bob*=2
        count_years+=1
    print(count_years)
