
import random
#HIGH LOW CARD GAME, BUT IN PYTHON
print("welcome to High Low Card Game")
#class of 52 cards
class DeckofCards:
    def __init__(self, suits, value, name):
        self.name = name
        self.suits = suits
        self.value = value
#initalizing list of 52 cards
list = []
#creting card list 
def create_list(): 
    list.append(DeckofCards('SPADES', 1, 'ACE OF SPADES'))
    list.append(DeckofCards('SPADES', 2, 'TWO OF SPADES'))
    list.append(DeckofCards('SPADES', 3, 'THREE OF SPADES'))
    list.append(DeckofCards('SPADES', 4, 'FOUR OF SPADES'))
    list.append(DeckofCards('SPADES', 5, 'FIVE OF SPADES'))
    list.append(DeckofCards('SPADES', 6, 'SIX OF SPADES'))
    list.append(DeckofCards('SPADES', 7, 'SEVEN OF SPADES'))
    list.append(DeckofCards('SPADES', 8, 'EIGHT OF SPADES'))
    list.append(DeckofCards('SPADES', 9, 'NINE OF SPADES'))
    list.append(DeckofCards('SPADES', 10, 'TEN OF SPADES'))
    list.append(DeckofCards('SPADES', 11, 'JACK OF SPADES'))
    list.append(DeckofCards('SPADES', 12, 'QUEEN OF SPADES'))
    list.append(DeckofCards('SPADES', 13, 'KING OF SPADES'))
    list.append(DeckofCards('HEARTS', 1, 'ACE OF HEARTS'))
    list.append(DeckofCards('HEARTS', 2, 'TWO OF HEARTS'))
    list.append(DeckofCards('HEARTS', 3, 'THREE OF HEARTS'))
    list.append(DeckofCards('HEARTS', 4, 'FOUR OF HEARTS'))
    list.append(DeckofCards('HEARTS', 5, 'FIVE OF HEARTS'))
    list.append(DeckofCards('HEARTS', 6, 'SIX OF HEARTS'))
    list.append(DeckofCards('HEARTS', 7, 'SEVEN OF HEARTS'))
    list.append(DeckofCards('HEARTS', 8, 'EIGHT OF HEARTS'))
    list.append(DeckofCards('HEARTS', 9, 'NINE OF HEARTS'))
    list.append(DeckofCards('HEARTS', 10, 'TEN OF HEARTS'))
    list.append(DeckofCards('HEARTS', 11, 'JACK OF HEARTS'))
    list.append(DeckofCards('HEARTS', 12, 'QUEEN OF HEARTS'))
    list.append(DeckofCards('HEARTS', 13, 'KING OF HEARTS'))
    list.append(DeckofCards('DIAMONDS', 1, 'ACE OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 2, 'TWO OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 3, 'THREE OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 4, 'FOUR OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 5, 'FIVE OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 6, 'SIX OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 7, 'SEVEN OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 8, 'EIGHT OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 9, 'NINE OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 10, 'TEN OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 11, 'JACK OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 12, 'QUEEN OF DIAMONDS'))
    list.append(DeckofCards('DIAMONDS', 13, 'KING OF DIAMONDS'))
    list.append(DeckofCards('CLUBS', 1, 'ACE OF CLUBS'))
    list.append(DeckofCards('CLUBS', 2, 'TWO OF CLUBS'))
    list.append(DeckofCards('CLUBS', 3, 'THREE OF CLUBS'))
    list.append(DeckofCards('CLUBS', 4, 'FOUR OF CLUBS'))
    list.append(DeckofCards('CLUBS', 5, 'FIVE OF CLUBS'))
    list.append(DeckofCards('CLUBS', 6, 'SIX OF CLUBS'))
    list.append(DeckofCards('CLUBS', 7, 'SEVEN OF CLUBS'))
    list.append(DeckofCards('CLUBS', 8, 'EIGHT OF CLUBS'))
    list.append(DeckofCards('CLUBS', 9, 'NINE OF CLUBS'))
    list.append(DeckofCards('CLUBS', 10, 'TEN OF CLUBS'))
    list.append(DeckofCards('CLUBS', 11, 'JACK OF CLUBS'))
    list.append(DeckofCards('CLUBS', 12, 'QUEEN OF CLUBS'))
    list.append(DeckofCards('CLUBS', 13, 'KING OF CLUBS'))
#Function of shuffling cards
def shuffle_list():
    random.shuffle(list)


create_list()
shuffle_list()
fc = 0
sc = 1
score = 0

first_card = list[fc].name
f_c = list[fc].value
second_card = list[sc].name
s_c = list[sc].value
playing = True
while playing:
    print(first_card)
    answer =  input("NEXT CARD IS HIGH OR LOW? ")
    if answer.lower() == "high":
        if s_c > f_c:
            print("Correct")
            fc = fc +1
            sc = sc +1
            score = score +1
            first_card = list[fc].name
            f_c = list[fc].value
            second_card = list[sc].name
            s_c = list[sc].value
            print("SCORE: ", score)
        else:
            print("GAMEOVER")
            print("Total Score: ", score)
            playing = False
    if answer.lower() == "low":
        if s_c < f_c:
            print("Correct")
            fc = fc +1
            sc = sc +1
            score = score +1
            first_card = list[fc].name
            f_c = list[fc].value
            second_card = list[sc].name
            s_c = list[sc].value
            print("SCORE: ", score)
        else:
            print("GAMEOVER")
            print("Total Score: ", score)
            playing = False

                

       
        
        



