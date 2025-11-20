
name=list(input('enter the word that you want to use to chalenge \n'))
name_guessed=[]
avoid_duplicat=[]
for i in range(len(name)):
    name_guessed.append('_')
    avoid_duplicat.append('*')
attempt =0
exclude=[]
while attempt <5 and name_guessed!=name:
    guess=input('enter the letter that u think it exist \n')
    
    if guess in name:
        if guess in name_guessed:
            for i in range(len(name_guessed)):
                if name[i]==guess and i not in exclude :
                    name_guessed[i]=guess
                    exclude.append(i)
                    print(f'the exclude list its {exclude}')
                    break

            
            print(f'you got {"".join(name_guessed)}')
            print('-----------------------------')

        else:
            name_guessed[name.index(guess)]=guess
            exclude.append(name.index(guess))
            print(f'the exclude list its {exclude}')
            print(f'you got {"".join(name_guessed)}')
            print('-----------------------------')
    else:
        attempt+=1
        print(f'you got {"".join(name_guessed)}')
        print(f'the exclude list its {exclude}')
        print('-----------------------------')


else:
    print(f'game finich you got {"".join(name_guessed)}')    