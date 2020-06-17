# -*- coding: utf-8 -*-

def main():
    import random
    
    #starting money
    money=1000
    

    #presentation
    print('Welcome to the roulette game! \nYou have 1000 dollars and can choose a number between 0 and 49 \nLets play!')
 

    def bet(moneyy):
        nonlocal money
        
        #to get the bet number and money
        betNumber=int(input('What is your bet number?'))
        while betNumber>49 or betNumber<0:
            print('the bet number should be between 0 and 49')
            betNumber=int(input('What is your bet number?'))

        betMoney=int(input('How much do you want to bet?'))
    
        #to verify the player's money
        while betMoney>money:
            print('You dont have that money!')
            betMoney=int(input('How much do you want to bet?'))
    
        #to cash the bet money
        money-=betMoney
        
        #to generate a random number
        sortedNumber= random.randint(0, 49)
        if betNumber==sortedNumber:
            money+=(betNumber*50)
            print('You win!!!, now you have',money,'dollars')
        else:
            print('You lose! The sorted number was', sortedNumber,'. \nNow you have',money,'dollars.')

    while money>0:
        bet(money)
        
    if money==0:
        print('Stop! You dont have money!')
main()
