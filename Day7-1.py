challenger_input=input('enter your text\n')
empty_gues=[]
game_count=0
excluded=[]
for i in range(len(challenger_input)):
    empty_gues.append('-')
while game_count !=4 or challenger_input==empty_gues:
    users_gues=input('enter your gues letter \n')
    for i in range(len(challenger_input)):
        print(f'{i}')
        if users_gues== challenger_input[i] and i not in excluded :
            empty_gues[i]=users_gues
            excluded.append(i)
            break
        elif users_gues not in challenger_input :
            game_count+=1
            break
    print(f'you got {"".join(empty_gues)} stil have {4-game_count} try\n')
if challenger_input==empty_gues:
    print(f'game finiched you have got it correct {{empty_gues}}')
else:
    print('game finiched you lose')