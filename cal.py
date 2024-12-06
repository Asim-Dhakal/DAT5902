import random 
Card=[1,2,3,4,5,6,7,8,9,10,11,12,13]
dice= random.randint(1,6)
dice2=random.randint(1,6)

Rcard=random.choice(Card)
sumdice = dice + dice2

if sumdice > Rcard:
    print('dice win')
elif Rcard>sumdice:
    print('cards win')
else: 
    print('Its a draw')
    

