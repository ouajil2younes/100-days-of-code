from os import system

bids={}
next=True
winer_name=''
winer_bid=0
while next:
    name=input('what is your name \n')
    bid=int(input('what us your bid\n'))
    bids[name]=bid
    check=input('are ther any other bidders ? type \'y\' for yes and \'n\' for no\n')
    if check=='n':
        next=False
    elif check=='y':
        system("cls")
for key in bids:
    if winer_bid<=bids[key]:
        winer_bid=bids[key]
        winer_name=key
print(f'the winer its {winer_name}  with a bid of {winer_bid} \n')