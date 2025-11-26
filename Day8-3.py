origin=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
word_to_enc=input('enter the word that u want to encode\n')
encoded_list=[]
encode_by=int(input('enter te number that u wont to use for the encode'))
#get the id of the position of the letter that the user entred
for j in range(len(word_to_enc)) :
    for i in range(len(origin)):
        if word_to_enc[j]==origin[i]:
            if i+encode_by<=25:
                print(f'i={i}  encode_by={encode_by}')
                print(f'we got i+encode_by<=26 {origin[i+encode_by]}')
                encoded_list.append(origin[i+encode_by])
            elif i+encode_by>25:
                count=24+i-encode_by
                print(f'-------- i={i} \n count={count} \n  encode_by={encode_by}')
                encoded_list.append(origin[count])
                print(f'we got  i+encode_by>26 {origin[count]}')

print(f'resolt {encoded_list}')
    