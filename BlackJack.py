import random
import os
import sys
import time

sleep_time = 3
os.system("clear")

print("\n"*3)
Suits = ["\u2663", "\u2665", 
         "\u2666", "\u2660"] 

Ranks = ['A', '2', '3', '4', '5', 
         '6', '7', '8', '9', '10', 
         'J', 'Q', 'K']

playingCards = []
Values = []
for i in range (1,11):
    Values.append(i)
      
for a in range(3):
    Values.append(10)
Values = Values*4

for i in Suits:
    for a in range(13) :
      playingCards.append(Ranks[a]+i)
     
      
playingCardsWithValues = {}

for i in playingCards:
    for a in range(len(playingCards)):
      playingCardsWithValues[playingCards[a]] = Values[a]
      
Aces=["A♣","A♥","A♦","A♠"]
for a in Aces:
    playingCardsWithValues[a] = 11

#print(playingCards)
#print(playingCardsWithValues) 

pc = playingCardsWithValues.copy()


playing_deck = 4*playingCards

playerFirstCard = random.choice(playing_deck)
playing_deck.remove(playerFirstCard)

dealerFirstCard = random.choice(playing_deck)
playing_deck.remove(dealerFirstCard)


playerSecondCard = random.choice(playing_deck)
playing_deck.remove(playerSecondCard)

dealerSecondCard = random.choice(playing_deck)
playing_deck.remove(dealerSecondCard)



player_total_1 = 0
player_total_2 = 0

if playerFirstCard in Aces and playerSecondCard in Aces:
    player_total_1 += 12
    player_total_2 += 2
elif playerFirstCard in Aces or playerSecondCard in Aces:
    if playerFirstCard in Aces:    
        player_total_1 += (11 + pc[playerSecondCard])
        player_total_2 += (1 + pc[playerSecondCard])
    else:
        player_total_1 += (11 + pc[playerFirstCard])
        player_total_2 += (1 + pc[playerFirstCard])
else:
    player_total_1 += (pc[playerFirstCard] + pc[playerSecondCard])
    player_total_2 += (pc[playerFirstCard] + pc[playerSecondCard])

dealer_total_1 = 0
dealer_total_2 = 0

if dealerFirstCard in Aces:
    dealer_total_1 += 11
    dealer_total_2 += 1
else:
    dealer_total_1 += pc[dealerFirstCard]
    dealer_total_2 = dealer_total_1

print(f"Dealers Cards:{dealerFirstCard} ?")
if dealer_total_1 == dealer_total_2:
    print("Dealer total:", dealer_total_1)
else:
    print("Dealer total:", dealer_total_1, "/", dealer_total_2)

print()
print(f"Your Cards :{playerFirstCard} {playerSecondCard}")

if player_total_1 == player_total_2 or player_total_1 == 21:
    print("Player total:", player_total_1)
else:
    print("Player total:", player_total_1, "/", player_total_2)


drawn_cards = []

finish = False

while not finish and (player_total_1 < 21 or player_total_2 < 21) and player_total_1 != 21:
    print()
    print("1: Hit")
    print("2: Stand")
    choice = int(input("Enter your choice: "))
    time.sleep(1)
    
    if choice == 1:
        new_card = random.choice(playing_deck)
        playing_deck.remove(new_card)
        
        is_ace = new_card in Aces
        
        
        # First two cars are not ace
        if player_total_1 == player_total_2:
            
            # First two cards sum >= 11
            if player_total_1 >= 11:
                
                # New card is ace
                if is_ace:
                    player_total_1 += 1
                    player_total_2 += 1
                # New card is not ace
                else:
                    player_total_1 += pc[new_card]
                    player_total_2 += pc[new_card]
                    
            # First two cards < 11
            else:
                if is_ace:
                    player_total_1 += 11
                    player_total_2 += 1
                else:
                    player_total_1 += pc[new_card]
                    player_total_2 += pc[new_card]
                
        
        # First two cards have ace
        else:
            if is_ace:
                player_total_1 += 1
                player_total_2 += 1
            else:
                player_total_1 += pc[new_card]
                player_total_2 += pc[new_card]
        
        drawn_cards.append(new_card)
        
        print(f"Your Cards :{playerFirstCard} {playerSecondCard}", end=" ")
        
        for i in drawn_cards:
            print(i, end=" ")
        print()
        

        if player_total_1 == player_total_2 or player_total_1 == 21:
            print("Player total:", player_total_1)
        elif player_total_1 > 21:
            print("Player total:", player_total_2)
        else:
            print("Player total:", player_total_1, "/", player_total_2)
        
    else:
        finish = True
       
       
       
final_total = None

if player_total_1 > 21 and player_total_2 > 21:
    print("You lost.")
    sys.exit(0)

elif player_total_1 <= 21 and player_total_2 <= 21:
    final_total = max(player_total_1, player_total_2)
    
else:
    final_total = player_total_2


print("Your total:", final_total)

if dealerSecondCard in Aces:
    if dealer_total_1 == dealer_total_2:
        dealer_total_1 += 11
        dealer_total_2 += 1
    else:
        dealer_total_1 += 1
        dealer_total_2 += 1
else:
    dealer_total_1 += pc[dealerSecondCard]
    dealer_total_2 += pc[dealerSecondCard]
    
print()
print("Dealer cards:", dealerFirstCard, dealerSecondCard)
if dealer_total_1 == dealer_total_2:
    print("Dealer total:", dealer_total_1)
else:
    print("Dealer total:", dealer_total_1, "/", dealer_total_2)
print()
time.sleep(sleep_time)

dealer_total = dealer_total_1
new_cards = [dealerFirstCard, dealerSecondCard]
while dealer_total_1 < 17 or (dealer_total_1 > 21 and dealer_total_2 < 17):
    new_card = random.choice(playing_deck)
    playing_deck.remove(new_card)
    new_cards.append(new_card)
    
    is_ace = new_card in Aces
    
    
    if dealer_total_1 == dealer_total_2:
        if is_ace:
            dealer_total_1 += 11
            dealer_total_2 += 1
        else:
            dealer_total_1 += pc[new_card]
            dealer_total_2 += pc[new_card]
            
    else:
        if is_ace:
            dealer_total_1 += 1
            dealer_total_2 += 1
        else:
            dealer_total_1 += pc[new_card]
            dealer_total_2 += pc[new_card]
    
    print("Dealers card:", end=" ")
    for i in new_cards:
        print(i, end=" ")
    print()
    
    if dealer_total_1<=21 and dealer_total_1>=17:
        print("Dealer total:", dealer_total_1)
        dealer_total = dealer_total_1
    elif dealer_total_2<=21 and dealer_total_2>=17:
        print("Dealer total:", dealer_total_2)
        dealer_total = dealer_total_2
    else:
        if dealer_total_1 == dealer_total_2:
            dealer_total = dealer_total_1
            print("Dealer total:", dealer_total_1)
        else:
            dealer_total = dealer_total_1
            print("Dealer total:", dealer_total_1, "/", dealer_total_2)
    print()
    
    time.sleep(sleep_time)

if dealer_total > 21:
    print("You win.")

elif dealer_total > final_total:
    print("House wins.")
    
elif dealer_total == final_total:
    print("Tie.")
else:
    print("You win.")

