import random
RPS=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
sh=int()
countH=0
countC=0
while True:
    if countH==2:
        print('goooood for you human ')
        break
    elif countC==2:
        print('robot')
        break
    sh=int(input('enter 0 for rock or 1 for paper or 2 scissers '))
    game_tools=random.randint(0,2)
    if game_tools== 0 and sh==0:
        print(f'equal - computer shose {RPS[0]} you chose {RPS[0]}')
    elif game_tools== 0 and sh==1:
        print(f'you win -computer shose {RPS[0]} you chose {RPS[1]}')
        countH+=1
    elif game_tools== 0 and sh==2:
        print(f'computer win -computer shose {RPS[0]} you chose {RPS[2]}')
        countC+=1

    elif game_tools== 1 and sh==0:
        print(f'computer win -computer shose {RPS[1]} you chose {RPS[0]}')
        countC+=1
    elif game_tools== 1 and sh==1:
        print(f'equal -computer shose {RPS[1]} you chose {RPS[1]}')
    elif game_tools== 1 and sh==2:
        print(f'you win -computer shose {RPS[1]} you chose {RPS[2]}')
        countH+=1
        
    elif game_tools== 2 and sh==0:
        print(f'you win -computer shose {RPS[2]} you chose {RPS[0]}')
        countH+=1
    elif game_tools== 2 and sh==1:
        print(f'computer win -computer shose {RPS[2]} you chose {RPS[1]}')
        countC+=1
    elif game_tools== 2 and sh==2:
        print(f'equal -computer shose {RPS[2]} you chose {RPS[2]}')

