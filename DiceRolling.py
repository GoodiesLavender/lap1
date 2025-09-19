
import random
MIN = 1
MAX = 6

def main():
    agian = 'y'
    while agian == 'y' or agian == 'Y':
        print ('Rolling the dice ...')
        print ('The values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        dice1 = random.randint(MIN, MAX)
        dice2 = random.randint(MIN, MAX)

        if dice1 > dice2:
            print('Dice 1 is The Winder!')
            elif dice2 > dice1:
                print('Dice 2 is The Winer!')
                else:
                    print('It is a tie!')
    
        agian = input ('Roll them agian? (y=yes): ')
        
        

    
