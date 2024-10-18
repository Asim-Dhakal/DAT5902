
# the function to check if input is even 
def NumberIsEven(Number):
    if type(Number) != int:
        return False

    if Number % 2 == 0:
        return True 
    else:
        return False 

