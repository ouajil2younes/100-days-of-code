import random
cartss = {
    1: {  # suit 1 = hearts
        1: "A♥", 2: "2♥", 3: "3♥", 4: "4♥", 5: "5♥", 6: "6♥",
        7: "7♥", 8: "8♥", 9: "9♥", 10: "10♥", 11: "J♥", 12: "Q♥", 13: "K♥"
    },
    2: {  # suit 2 = diamonds
        1: "A♦", 2: "2♦", 3: "3♦", 4: "4♦", 5: "5♦", 6: "6♦",
        7: "7♦", 8: "8♦", 9: "9♦", 10: "10♦", 11: "J♦", 12: "Q♦", 13: "K♦"
    },
    3: {  # suit 3 = clubs
        1: "A♣", 2: "2♣", 3: "3♣", 4: "4♣", 5: "5♣", 6: "6♣",
        7: "7♣", 8: "8♣", 9: "9♣", 10: "10♣", 11: "J♣", 12: "Q♣", 13: "K♣"
    },
    4: {  # suit 4 = spades
        1: "A♠", 2: "2♠", 3: "3♠", 4: "4♠", 5: "5♠", 6: "6♠",
        7: "7♠", 8: "8♠", 9: "9♠", 10: "10♠", 11: "J♠", 12: "Q♠", 13: "K♠"
    }
}
user_carts=[]
dealer_carts=[]
def sum_micro(symbol,sum_resolt,aces_count):# rake "10♠" as input
    number_of_cart=symbol[:-1]#get all the elemts expect the last
    print(f'sum is caled and we have {symbol} and {sum_resolt} and {aces_count} aaaand {number_of_cart}')
    if  number_of_cart=='A' :
        sum_resolt.append(11)
        aces_count+=1
    elif number_of_cart=='J':
        sum_resolt.append(10)  
    elif number_of_cart=='Q':
        sum_resolt.append(10)  
    elif number_of_cart=='K':
        sum_resolt.append(10) 
    elif int(number_of_cart)>=2 and int(number_of_cart)<=10:
        sum_resolt.append(int(number_of_cart))  
    print(f'sum is finiched and we have {symbol} and {sum_resolt} and {aces_count}')
    return sum_resolt,aces_count
    
def sum_carts_values(symbol_entred):
    aces_count=0
    sum_resolt=[]
    print(f'befor the loop {symbol_entred}')
    for symbol in symbol_entred: 
            if symbol[-1]=='♠' :
                sum_resolt,aces_count=sum_micro(symbol,sum_resolt,aces_count)
            elif symbol[-1]=='♥' :
                sum_resolt,aces_count=sum_micro(symbol,sum_resolt,aces_count)           
            elif symbol[-1]=='♣' :
                sum_resolt,aces_count=sum_micro(symbol,sum_resolt,aces_count)           
            elif symbol[-1]=='♦' :
                sum_resolt,aces_count=sum_micro(symbol,sum_resolt,aces_count)
            res=sum(sum_resolt)                         
    while res>21 and aces_count > 0:
        res-=10 
    return res 
 
def get_cart():#give you a random cart (iner) with its outer the outer (its the shosen type of carts)
    outer=random.choice(list(cartss.keys()))#1 2 3 4
    iner_key=random.choice(list(cartss[outer].keys()))#1 2 3 4 5 6 7 8 9
    res=cartss[outer].pop(iner_key)
    return res
play_again=True
for i in range(2):
    user_carts.append(get_cart())
    dealer_carts.append(get_cart())



while play_again:
    print('----------------------------------------------------------------')
    print(f'user_cart {user_carts}')
    print(f'your carts are {user_carts} | total : {sum_carts_values(user_carts)} \nDealers cart is {dealer_carts[0]} | total {sum_carts_values(dealer_carts[0])} ')
    chois=input('Do you want to get another cart pres (1) or to stop here pres (2) ')
    if chois=='1':
        user_carts.append(get_cart())
        if sum_carts_values(user_carts)>21:
            print(f'you lose \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)} ')
        elif sum_carts_values(user_carts)==21 and sum_carts_values(dealer_carts)==21:
            print(f'equal \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)}\ndealer carts are : {dealer_carts} \nhis total is : {sum_carts_values(dealer_carts)}')
        elif sum_carts_values(user_carts)==21 and sum_carts_values(dealer_carts)!=21:
            print(f'you win \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)} ')
    if chois=='2':
        while sum_carts_values(dealer_carts)<17:
            dealer_carts.append(get_cart())
        if sum_carts_values(dealer_carts)>21:
            print(f'you win \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)}\ndealer carts are : {dealer_carts} \nhis total is : {sum_carts_values(dealer_carts)}')
        elif sum_carts_values(dealer_carts)<sum_carts_values(user_carts):
            print(f'you win \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)}\ndealer carts are : {dealer_carts} \nhis total is : {sum_carts_values(dealer_carts)}')
        elif sum_carts_values(dealer_carts)>sum_carts_values(user_carts):
            print(f'dealer win \nyour carts are : {user_carts} \nyour total is : {sum_carts_values(user_carts)}\ndealer carts are : {dealer_carts} \nhis total is : {sum_carts_values(dealer_carts)}')
#need the case wher if the user hit a black jack at first