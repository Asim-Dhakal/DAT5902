import random 

N_min = 1 
N_max = 100 
N_rand= random.randint(1,100)

i = 1
Continue = 1 

while Continue == 1:
    guess= int(input('guess a number'))

    if (guess>N_rand):
        print('Too High')
        i += 1 
    elif (guess<N_rand):
        print('Too low')
        i += 1
    else:
        print('Success! Guessed in'+str(i)+'attempts')
        Continue = 0     
