answear=input('hello ther want to start play pleat shose Left or Right (type the first leter of your answear) ').lower()
if answear=='l':
    answear=input('you found a lake wnat to Swim or Wait the boat')
    if answear=='w':
        answear=input('which door Red Rlue or Yellow')
        if answear=='y':
            print('gooooooood')
        else:
            print('game over')
    else:
        print('gameover')
else:
    print('game over')