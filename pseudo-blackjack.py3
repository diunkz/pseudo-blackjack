import random

#function to remove cards
def removeCards(number,deck):
    deck = deck.remove(number)

# function to add cards
def addCards(number,deck):
    deck = deck.append(number)
    
# function to generate a random card from deck
def randomCard(deck):
    return random.choice(deck)

# function to start the game
def start(p1deck, p2deck, deck):
    #generating random deck cards
    randomCardOne = randomCard(deck)
    randomCardTwo = randomCard(deck)

    #removing random cards from deck
    removeCards(randomCardOne,deck)
    removeCards(randomCardTwo,deck)

    #adding cards to player 1 list
    addCards(randomCardOne,playerOne)
    addCards(randomCardTwo,playerOne)

    #generating random deck cards
    randomCardOne = randomCard(deck)
    randomCardTwo = randomCard(deck)

    #adding cards to player 1 list
    addCards(randomCardOne,playerTwo)
    addCards(randomCardTwo,playerTwo)

    #removing random cards from deck
    removeCards(randomCardOne,deck)
    removeCards(randomCardTwo,deck)


#creating lists(deck, playerOne, playerTwo)
deck = list(x for x in range(1,11))*4
for x in range(4*4):  deck.append(10)
playerOne = []
playerTwo = []

start(playerOne,playerTwo,deck)

print("\n---------------------------------------")
print("\nPlayer One Hand: ", playerOne, "->", sum(playerOne), "\nPlayer Two Hand: ", playerTwo, "->",sum(playerTwo))

#variables to stop
stopOne = 1
stopTwo = 1
conditionOne = True
conditionTwo = True
bustedOne = False
bustedTwo = False
while((stopOne+stopTwo)!=0):
    if (stopOne and conditionOne):
        conditionOne = True
        stopOne = int(input(("\nPlayer 1, press:\n\t\t1 -> Hit!\n\t\t2 -> Stand!\n\t\t  -> ")))
        if (stopOne==2): stopOne = 0
        elif (stopOne == 1):
            randomCardOne = randomCard(deck)
            addCards(randomCardOne,playerOne)
            removeCards(randomCardOne,deck)
            if (sum(playerOne)>21):
                bustedOne = True
                conditionOne = False
                stopOne = 0
                stopTwo = 0
        else:  conditionTwo = False
    print("\nPlayer One Hand: ", playerOne, "->", sum(playerOne))

    conditionOne = True

    if (stopTwo and conditionTwo):
        conditionTwo = True
        stopTwo = int(input(("\nPlayer 2, press:\n\t\t1 -> Hit!\n\t\t2 -> Stand!\n\t\t  -> ")))
        if (stopTwo==2): stopTwo = 0
        elif (stopTwo == 1):
            randomCardTwo = randomCard(deck)
            addCards(randomCardTwo,playerTwo)
            removeCards(randomCardTwo,deck)
            if (sum(playerTwo)>21):
                bustedTwo = True
                conditionTwo = False
                stopOne = 0
                stopTwo = 0
        else: conditionOne = False
    print("Player Two Hand: ", playerTwo, "->", sum(playerTwo))
    print("\n---------------------------------------")
    conditionTwo = True

print("\n------------------END------------------")
print("\n---------------------------------------")
if  (bustedTwo == True): print("\nplayer 2 busted | player 1 wins\n")
elif(bustedOne == True): print("\nplayer 1 busted | player 2 wins\n")
elif (sum(playerOne) > sum(playerTwo)): print("\nplayer 1 wins\n")
elif (sum(playerTwo) > sum(playerOne)): print("\nplayer 2 wins\n")
else: print("\nDRAW\n")
