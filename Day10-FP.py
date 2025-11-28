
again=False
def devide(number1,number2):
        return   number1/number2
def multip(number1,number2):
        return   number1*number2
def add(number1,number2):
        return  number1+number2
def sub(number1,number2):
        return   number1-number2
resolt=0
while True :
    number1=int(input('enter your first number '))
    op=input('enter your operator ')
    number2=int(input('enter your second number '))
    if op=='/':
        if number2==0:
            print('incorrect we cant devide by 0')
        elif number2!=0 :
            resolt+=devide(number1,number2)
            print(f'{number1} {op} {number2} = {resolt}')
    elif op=='*':
            resolt+=multip(number1,number2)
            print(f'{number1} {op} {number2} = {resolt}')
    elif op=='+':   
            resolt+=add(number1,number2)
            print(f'{number1} {op} {number2} = {resolt}')
    elif op=='-':     
            resolt+=sub(number1,number2)
            print(f'{number1} {op} {number2} = {resolt}')
    chois=input(f'wold you like to continu with your last resolt {resolt} enter Y or start new calculation emter N')
    if chois=='n':
        again=False
        resolt=0 

        


