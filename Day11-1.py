import random
carts=[1,2,3,4,5,6,7,8,9,10,11,12,13]*4
cartss = {1: "A♥",2: "2♥",3: "3♥",4: "4♥",5: "5♥",6: "6♥",7: "7♥",8: "8♥",9: "9♥",10: "10♥",11: "J♥",12: "Q♥",13: "K♥"}
user_carts=[]
dealer_carts=[]
def get_random_user():
    user_chois_random =random.choice(carts)
    #in case we got un ace we count it as 1 or 10 depend on if its more than 21 or no
    
    if user_chois_random == 1:
        user_carts.append(11)
        carts.remove(1)
    elif user_chois_random == 12:
        user_carts.append(10)
        carts.remove(12)
    elif user_chois_random == 13:
        user_carts.append(10)
        carts.remove(13)
    else:
        user_carts.append(user_chois_random)   
        carts.remove(user_chois_random)
  
def get_random_dealer():
    dealer_chois_random =random.choice(carts)
    #in case we got un ace we count it as 1 or 10 depend on if its more than 21 or no
    if dealer_chois_random == 1:
        if sum(dealer_carts)>=21:
            dealer_carts.append(1)
            carts.remove(1)
        elif sum(dealer_carts)<=21:
            dealer_carts.append(11)
            carts.remove(1)
    elif dealer_chois_random == 12:
        dealer_carts.append(10)
        carts.remove(12)
    elif dealer_chois_random == 13:
            dealer_carts.append(10)
            carts.remove(13)
    else:
        dealer_carts.append(dealer_chois_random)
        carts.remove(dealer_chois_random)

def get_random():
    get_random_user()
    get_random_dealer()
        
get_random()
get_random()
while True:
    print('------------------------------------------------------')
    if sum(user_carts)==21 and len(user_carts)==2 :
        print(f'black jack you win you got {sum(user_carts)}')
    elif sum(dealer_carts)==21 and len(dealer_carts)==2 :
        print(f'black jack dealer win he got {sum(dealer_carts)}')
    elif sum(dealer_carts)==21 and sum(user_carts)==21:
        print(f'they are equals')
    else:
        print(f'computers carts are {cartss[dealer_carts[0]]} with total {dealer_carts[0]} ')
        print(f'your total is {sum(user_carts)} your carts are ' , end="")
        for i in user_carts:
            print(f'{cartss[i]} ', end="")

    user_chois=int(input('enter your chois is it a HIT pres 1 or STOP pres 0 '))
    if user_chois==1:#hit
        get_random_user()    
        if sum(user_carts)>21 and 11 not in user_carts :
            print(user_carts[-1])
            print(f'you lose with a total {sum(user_carts)}')
            break
        elif  sum(user_carts)>21 and 11 in user_carts :
                while sum(user_carts)>21 :
                    if 11 in user_carts :
                        get_index=user_carts.index(11)
                        user_carts[get_index]=1
                    else:
                        break
        elif sum(user_carts)==21:
            print(f'you win with a total {sum(user_carts)}')
            break
        elif sum(user_carts)<21:
            print(f'you got {cartss[user_carts[-1]]} with a total {sum(user_carts)}') 
        
    elif user_chois==0:#stop
        while  sum(dealer_carts)<=17:
            get_random_dealer()

        if sum(dealer_carts)>21:
            print(f'you win with a total {sum(dealer_carts)} dealer carts are ', end="")
            for i in dealer_carts:
                print(f'{cartss[i]} ', end="")
            break
        
        elif sum(dealer_carts)<sum(user_carts):
            print(f'user win  user={sum(user_carts)}  dealer={sum(dealer_carts)} ')
            break
        elif sum(dealer_carts)>sum(user_carts):
            print(f'dealer win  user={sum(user_carts)}  dealer={sum(dealer_carts)}  ')
            for i in dealer_carts:
                print(f'{cartss[i]} ', end="")
            break
        elif sum(dealer_carts)==sum(user_carts):
            print(f'dealer and user are equal user={sum(user_carts)} and  dealer={sum(dealer_carts)} ')
            break