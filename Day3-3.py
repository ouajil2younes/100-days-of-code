size=''
pepperonie=''
extra_cheese=''
print('welcom to our python pizza')
while True :
    if size not in ['s','m','l']:
        size=input('enter your pizza size is it \'s\' for smal or \'m\' for medieum or \'l\' for large or x to escape ').lower()
        continue
    if pepperonie not in ['y','n']:
        pepperonie=input('do you wanr pepperonee y or n ').lower()
        continue
    if extra_cheese not in ['y','n']:
        extra_cheese=input('do you want extra cheese y or n').lower()
        continue
    else:
        break

pizza_prie=0
if size=='s':
    pizza_prie+=15
    if  pepperonie=='y':
        pizza_prie+=2
elif size=='m':
    pizza_prie+=20
    if  pepperonie=='y':
        pizza_prie+=3  
elif size=='l':
    pizza_prie+=25
    if  pepperonie=='y':
        pizza_prie+=3 
if extra_cheese=='y':
    pizza_prie+=1
print(f'your pizza its ready the price is {pizza_prie}')