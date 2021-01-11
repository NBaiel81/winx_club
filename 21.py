players=['baiel','nurjanat','akylbek','maksim','aigerim']
scores=[]
i=0
import random
while i<len(players):
    print(f'welocme!!!, {players[i]}')#inside{} peremenaya
    score=random.randint(2,11)+random.randint(2,11)
    score=random.randint(2,11)+random.randint(2,11)
    print(score)
    check=input("yes/no")
    while check=="yes":
        score+=random.randint(2,11)
        print(score)
        check=input('yes/no')
        if score>21:
            score=0

    scores.append(score)
    i+=1
max_scores=max(scores)
winner=players[scores.index(max_scores)]
print(f'winner:{winner}, with score {max_scores}')

