
again=False
def devide(number1,number2):
        if number2==0:
            print('incorrect we cant devide by 0')
            return 0
        elif number2!=0 : 
            return   number1/number2
def multip(number1,number2):
        return   number1*number2
def add(number1,number2):
        return  number1+number2
def sub(number1,number2):
        return   number1-number2
operation_dic={"+":add,
              "-":sub,
              "*":multip,
              "/":devide,}
resolt=0
while True :
    number1=float(input('enter your first number '))
    while True:
        op=input('enter your operator ')
        if op not in operation_dic:
            print('worng operator')
        elif op in operation_dic:  
            break
    
    number2=float(input('enter your second number '))
    resolt+=operation_dic[op](number1,number2)
    print(f'{number1} {op} {number2} = {resolt}')

    chois=input(f'wold you like to continu with your last resolt {resolt} enter Y or start new calculation emter N')
    if chois=='n':
        again=False
        resolt=0 

        


