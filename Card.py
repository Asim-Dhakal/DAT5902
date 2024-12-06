import random 

Card_Number_list=['A','2','3','4', '5','6','7' ,'8','9','10','J','Q','K']
Suit_List = ['S','H','D','C']

number_chosen = input('Chose a card number from A 2 3 4 5 6 7 8 9 10 J Q K ')
suit_chosen = input('Chose suit: S for spades, H for heart, D for diamond, C for club')

number_picked = Card_Number_list[random.randint(0,12)]
suit_picked = Suit_List[random.randint(0,3)]

while number_chosen not in Card_Number_list:
    print('invalid input')
    number_chosen = input('Chose a card number from A 2 3 4 5 6 7 8 9 10 J Q K ')
while suit_chosen not in Suit_List:
    print('invalid input')
    suit_chosen = input('Chose suit: S for spades, H for heart, D for diamond, C for club')

if number_chosen == number_picked and suit_picked == suit_chosen:
    print('You win!')
elif number_chosen == number_picked:
    print('Close, but not quite!')
elif suit_chosen == suit_picked:
    print('Good try') 
else:
    print('incorect')

                  