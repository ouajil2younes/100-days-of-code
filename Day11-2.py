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
play_again=True
user_carts={}
dealer_carts={}
ask_play_again=False

def sum_carts_values(dictinary_of_carts):
    dictionary_element_values=[]
    for i in range(len(dictinary_of_carts)):
        if dictinary_of_carts[i]==1:
            dictionary_element_values.append(11)
        elif dictinary_of_carts[i]==-1:
            dictionary_element_values.append(1)   
        elif dictinary_of_carts[i]>=2 and dictinary_of_carts[i]<=10:
             dictionary_element_values.append(dictinary_of_carts[i])
        elif dictinary_of_carts[i]==11:
             dictionary_element_values.append(10)
        elif dictinary_of_carts[i]==12:
             dictionary_element_values.append(10)
        elif dictinary_of_carts[i]==13:
             dictionary_element_values.append(10)
    return sum(dictionary_element_values)   

def translate_cart(iner,outer):#we enter a iner outer values and it give us ther real (symbol) 
        if iner==1 or iner==-1 :
            val='A'
        elif iner>=2 and iner<=10:
             val=iner
        elif iner==11:
             val="J"
        elif iner==12:
             val="Q"
        elif iner==13:
             val="K"
        #symbol     
        if outer==1:
            res=str(val)+'♥'
        elif outer==2:
            res=str(val)+'♦'
        elif outer==3:
            res=str(val)+'♣'
        elif outer==4:
            res=str(val)+'♠'
        return res    
def get_cart():
        outer_TurnOn=random.choice(list(cartss.keys()))#it will give you number betwen 1 an 4
        iner_TurnOn=random.choice(list(cartss[outer_TurnOn].keys()))#this will give you number betwen 1 and 13 
        cartss[outer_TurnOn].pop(iner_TurnOn)
        return outer_TurnOn,iner_TurnOn
    
#user get a cart
for i in range(2):
    outer_user,iner_user=get_cart()
    user_carts[iner_user]=translate_cart(iner_user,outer_user)
    #dealer get a cart
    outer_dealer,iner_dealer=get_cart()
    dealer_carts[iner_dealer]=translate_cart(iner_dealer,outer_dealer)
while play_again:
    print('----------------------------------------------------------------------------------------\n')
    print(f'Dealer has {list(dealer_carts.values())[-1]} with total {sum_carts_values([list(dealer_carts.keys())[-1]])} ')
    print(f'you have {" ".join(user_carts.values())} with a total of {sum_carts_values(list(user_carts.keys()))} ')
    chois=int(input('Do you want to get another cart pres 1 or stop pres 2 '))
    if chois==1:
        
        outer_user,iner_user=get_cart()
        user_carts[iner_user]=translate_cart(iner_user,outer_user)
        if  sum_carts_values(list(user_carts.keys())) >21:
            while sum_carts_values(list(user_carts.keys())) >21:
                ace = user_carts.get(1,"Unknown")
                if ace=='Unknown' and sum_carts_values(list(user_carts.keys())) <=21:
                    ask_play_again=True
                    break
                elif ace=='Unknown' and sum_carts_values(list(user_carts.keys())) >21:
                    print(f'you lose you with total carts of {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())}')
                    ask_play_again=True
                    break
                elif ace!='Unknown' and sum_carts_values(list(user_carts.keys())) >21:
                    user_carts.pop(1)
                    user_carts[-1]=translate_cart(iner=-1,outer=outer_user)
                elif ace!='Unknown' and sum_carts_values(list(user_carts.keys())) <=21:
                    ask_play_again=True
                    break
        elif sum_carts_values(list(user_carts.keys()))==21 and sum_carts_values(list(dealer_carts.keys()))==21:
                print(f'you are equals by a total of {sum_carts_values(list(user_carts.keys()))} your carts are {" ".join(user_carts.values())} Dealer carts {" ".join(dealer_carts.values())} ')
                ask_play_again=True
                break
        elif  sum_carts_values(list(user_carts.keys())) ==21 and sum_carts_values(list(dealer_carts.keys()))!=21 :
                print(f'black jack you win by {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())}')
                ask_play_again=True
                break
    elif chois==2:
        if  sum_carts_values(list(dealer_carts.keys())) <17:
            while sum_carts_values(list(dealer_carts.keys())) <17:
                    #dealer get a cart
                    outer_dealer,iner_dealer=get_cart()
                    dealer_carts[iner_dealer]=translate_cart(iner_dealer,outer_dealer)  
        
        if   sum_carts_values(list(dealer_carts.keys())) > 21:
            print(f'you win with a total of {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())} \n Delers have a total of {sum_carts_values(list(dealer_carts.keys()))} \n your carts are {" ".join(dealer_carts.values())}')
            ask_play_again=True
            break
        elif  sum_carts_values(list(dealer_carts.keys())) > sum_carts_values(list(user_carts.keys())):
            print(f'dealer win with a total of {sum_carts_values(list(dealer_carts.keys()))} \n your carts are {" ".join(dealer_carts.values())} \n user have a total of {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())}  ')
            ask_play_again=True
            break
        elif  sum_carts_values(list(dealer_carts.keys())) < sum_carts_values(list(user_carts.keys())):
            print(f'you win with a total of {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())} \n Delers have a total of {sum_carts_values(list(dealer_carts.keys()))} \n your carts are {" ".join(dealer_carts.values())}  ')
            ask_play_again=True
            break
        elif  sum_carts_values(list(dealer_carts.keys())) == sum_carts_values(list(user_carts.keys())):
            print(f'dealer and user are equal user total and carts are {sum_carts_values(list(user_carts.keys()))} \n your carts are {" ".join(user_carts.values())} \n Delers have a total of {sum_carts_values(list(dealer_carts.keys()))} \n your carts are {" ".join(dealer_carts.values())} ')
            ask_play_again=True
            break
    else:
        print('you entred a wrong caracter')
    if ask_play_again:
        play=True
    else:  
        play=False
