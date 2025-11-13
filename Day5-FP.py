# ✅ List of lowercase letters
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                     'u', 'v', 'w', 'x', 'y', 'z']

# ✅ List of uppercase letters
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                     'U', 'V', 'W', 'X', 'Y', 'Z']

# ✅ List of symbols
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', 
           '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', 
           ',', '.', '?', '/', '\\', '|', '~', '`']

# ✅ List of numbers from 1 to 9
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import random
lw_letters_count=int(input('how many lower case leters do you want in your password '))
lw_track=0
up_letters_count=int(input('how many uper case leters do you want in your password '))
up_track=0
symbols=int(input('how many symbols do you want in your password '))
sy_track=0
numbers=int(input('how many numbers do you want in your password '))
num_track=0
password=''
pass_generator=[numbers_list,symbols_list,uppercase_letters,lowercase_letters]
total_count=lw_letters_count+up_letters_count+symbols+numbers
while lw_track<lw_letters_count or up_track<up_letters_count or sy_track<symbols or num_track<numbers:

    select_rnd=random.randint(0,3)
    if select_rnd==0:
        chosen_letter=lowercase_letters[random.randint(0,len(lowercase_letters)-1)]

    elif select_rnd==1:
        chosen_letter=uppercase_letters[random.randint(0,len(uppercase_letters)-1)]

    elif select_rnd==2:
        chosen_letter=symbols_list[random.randint(0,len(symbols_list)-1)]

    elif select_rnd==3:
        chosen_letter=numbers_list[random.randint(0, len(numbers_list)-1)]      

    # chosen_letter=random.randint(0,len(pass_generator[0]+pass_generator[1]+pass_generator[2]+pass_generator[3]+pass_generator[4])+1)
    if chosen_letter in lowercase_letters and lw_track<lw_letters_count:
        password=password+ chosen_letter
        lw_track+=1

    elif chosen_letter in uppercase_letters and up_track<up_letters_count:
        password=password+chosen_letter
        up_track+=1

    elif chosen_letter in symbols_list and sy_track<symbols:
        password=password+chosen_letter
        sy_track+=1

    elif chosen_letter in numbers_list and num_track<numbers:
        password=password+str(chosen_letter)
        num_track+=1

print(f'your pass is {password}')
password=list(password)
random.shuffle(password)
print(f'your pass is {password}')
password=''.join(password)
print(f'your pass is {password}')


