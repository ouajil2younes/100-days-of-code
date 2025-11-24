import random
hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    game over
    """
]
lose_score=0
hang=''
blank=''
correct_letters=[]
game_over=True
word_list=["aardvark","baboon","camel"]
chosen_word=random.choice(word_list)
for i in range(len(chosen_word)):
    blank+='_'
print(blank)
print(f'the chosen its {chosen_word}')
while lose_score<=len(chosen_word) :
    users_input=input('enter your chosen letter\n').lower()
    display=''
    for letter in chosen_word:
        if users_input== letter:
            display+=users_input
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    if users_input not in chosen_word:
        print('we are here')
        lose_score+=1
        print(f'{lose_score}')
        hang=hangman_stages[lose_score]        
    print(f'resolt : {display} ')
    print(f'resolt : {hang} ')