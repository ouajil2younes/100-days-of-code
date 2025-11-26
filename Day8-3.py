origin=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
origin2=origin[::-1]
play=True
def encrypt(origin):
    word_to_enc=input('enter the message that you want to encode:\n')
    encoded_list=[]
    encode_by=int(input('entre your shift number \n'))
    for j in range(len(word_to_enc)) :
            for i in range(len(origin)):
                if word_to_enc[j]==origin[i]:
                    if i+encode_by<=25:
                        encoded_list.append(origin[i+encode_by])
                    elif i+encode_by>25:
                        count=(encode_by+i)%26
                        encoded_list.append(origin[count])
    resolt=''.join(encoded_list)
    print(f'yor encoded message is {resolt} ')
def decrypt(origin):
    word_to_enc=input('enter the message that you want to encode:\n')
    encoded_list=[]
    encode_by=int(input('entre your shift number \n'))
 #get the id of the position of the letter that the user entred
    for j in range(len(word_to_enc)) :
            for i in range(len(origin)):
                if word_to_enc[j]==origin[i]:
                    if i+encode_by<=25:
                        encoded_list.append(origin[i+encode_by])
                    elif i+encode_by>25:
                        count=(encode_by+i)%26
                        encoded_list.append(origin[count])
    resolt=''.join(encoded_list)
    print(f'yor encoded message is {resolt} ')
def play_again():
        play_chois=input('do you want to repeat again or exit pres \'y\' to continu or \'n\' to exit \n')
        if play_chois=='n':
            return False
        elif play_chois=='y':
            return True
while play:
    choisc=input('do you want to encode type \'e\' and if you want to decode enter \'d\':\n')
    if choisc=='e':
        encrypt(origin=origin)
        play=play_again()
    if choisc=='d':
        decrypt(origin=origin2)
        play=play_again()