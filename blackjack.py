import random
playerIn = True
dealerIn = True
print("\nPershendetje dhe mireseerdhet ne BGT casino!!\n")
depozit = input("Sa para don te kthesh ne chips?\n")

while int(depozit) < 10 :
    print("Shuma minimale eshte 10$")
    depozit = input("Sa para don te kthesh ne chips?\n")
    


print(depozit + "$ jane transferuar ne akontin tuaj.Faleminderit\n")
tavolina = input("\nShtyp 1 nese deshiron te ulesh ne tavolinen e blackjack!!\n")
if tavolina == "1":
    bet = input("Sa para deshironi te luani?\n")
    while bet > depozit or len(bet) == 0:
        print("Ti nuk ke mjafuteshem chips")
        bet = input("Sa para deshiron te luani?\n")
    if bet == depozit:
        allin = input("A jeni te sigurt qe doni te luani ALL IN?\n")
        if allin == "po" or allin == "Po" or allin == "PO" or allin == "1":
            print("\nJu po luani ALL IN\n")
    

            
    
    print("\nLoja po fillon!Beti yt eshte:" + bet + "$")
else:
    print("Diten e mire!Shpresoj te ktheheni perseri.")
    exit()
    
win = int(bet) + int(depozit)
loose = int(depozit) - int(bet)


#Letrat,Lojtari dhe Dealer
letrat = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
"J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", ]
doralojtarit = []
doradealerit = []

#mi qkep letrat
def dealCard(turn):
    card = random.choice(letrat)
    turn.append(card)
    letrat.remove(card)

#kalkulim i kartave

def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10 
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total 

#me gjet fitusin

def revealDealerHand():
    if len(doradealerit) == 2:
        return doradealerit[0]
    elif len(doradealerit) > 2:
        return doradealerit[0], doradealerit[1]

#loop per loj  

for _ in range(2):
    dealCard(doradealerit)
    dealCard(doralojtarit)
while playerIn or dealerIn:
    print(f"Dealer ka {revealDealerHand()} dhe ??")
    print(f"Ti ke {doralojtarit} qe bejne {total(doralojtarit)}")
    if playerIn:
        stayORhit = input("1: Stay\n2: Hit\n")
    if total(doradealerit) > 16:
        dealerIn = False
    else:
        dealCard(doradealerit)
    if stayORhit == "1" or stayORhit == "stay" or stayORhit == "Stay":
        playerIn = False
    else:
        dealCard(doralojtarit)
    if total(doralojtarit) >= 21:
        break
    elif total(doradealerit) >=21:
        break

if total(doralojtarit) == 21:
    print(f"\nTi ke {doralojtarit} per nje total nga 21 dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Blackjack!!Ti fitove!!")
    print(f"Llogaria jote eshte: {win}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
    
elif total(doradealerit) == 21:
    print(f"\nTi ke {doralojtarit} per nje total nga {total(doralojtarit)} dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Blackjack!!Dealeri fitoj!!")
    print(f"Llogaria jote eshte: {loose}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
    
    

elif total(doralojtarit) > 21:
    print(f"\nTi ke {doralojtarit} per nje total nga {total(doralojtarit)} dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Ti humbe!!Dealeri fitoj!!")
    print(f"Llogaria jote eshte: {loose}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
    

elif total(doradealerit) > 21:
    print(f"\nTi ke {doralojtarit} per nje total nga {total(doralojtarit)} dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Ti fitove!!Dealeri humbi!!")
    print(f"Llogaria jote eshte: {win}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
    
elif 21 - total(doradealerit) < 21 - total(doralojtarit):
    print(f"\nTi ke {doralojtarit} per nje total nga {total(doralojtarit)} dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Dealeri Fitoj!!")
    print(f"Llogaria jote eshte: {loose}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
    

elif 21 - total(doradealerit) > 21 - total(doralojtarit):
    print(f"\nTi ke {doralojtarit} per nje total nga {total(doralojtarit)} dhe dealer ka {doradealerit} per nje total nga {total(doradealerit)}")
    print("Ti fitove!!")
    print(f"Llogaria jote eshte: {win}$")
    vazhdo = input("Shtypni 1 nese deshironi te luani perseri.\nShtypni 2 nese deshironi te ndaloni.\n")
if vazhdo == "2":
    print("Shpresoj te ktheheni perseri!")
    exit()
    

    
    







