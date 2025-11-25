def calculate_love_score(name1,name2):
    full_name =name1+name2
    total1=0
    total2=0
    for letter in full_name.lower():
        print(letter)
        if letter in 'true':
            total1+=1
        if letter in 'love':
            total2+=1
    print(f'{total1}{total2}')
    
calculate_love_score("Kanye West", "Kim Kardashian")
