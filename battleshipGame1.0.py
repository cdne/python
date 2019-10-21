import random
import os
import time



board = []
os.system('clear')
ship = '''	
                                                                                        
            .                                                         
            _\____                                                    
           |_===__`.        ==/                                       
           \/  '---"\ _ _ _ _/                                        
     ______/_______/_|_|_|_|_|                                        
   _|---------------------==.`                                        
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                      

'''

def banner():
    os.system('clear')
    # defining game banner
    banner = '''

                                                                        🇧​  🇦​  🇹​  🇹​  🇱​  🇪​  🇸  ​🇭  🇮  ​🇵​

                                                                                 🇬  🇦  🇲  ​🇪​
    '''
    
    print(banner)
    print(ship)

# draw the board in list
for i in range(10):
    temp = []
    for j in range(10):
        temp.append("🅞 ")
    board.append(temp)

# settings board and printing it to users
def boardS():

    board[0][1] = "A "
    board[0][2] = "B "
    board[0][3] = "C "
    board[0][4] = "D "
    board[0][5] = "E "
    board[0][6] = "F "
    board[0][7] = "G "
    board[0][8] = "H "
    board[0][9] = "I "

    board[0][0] = "  "
    board[1][0] = "1 "
    board[2][0] = "2 "
    board[3][0] = "3 "
    board[4][0] = "4 "

    board[6][0] = "6 "
    board[7][0] = "7 "
    board[8][0] = "8 "
    board[9][0] = "9 "

    board[5][0] = "\n🇵 "
    board[5][1] = "🇱 "
    board[5][2] = "🇦 "
    board[5][3] = "🇾 "
    board[5][4] = "🇪 "
    board[5][5] = "🇷 "
    board[5][6] = " "
    board[5][7] = "🇹 "
    board[5][8] = "🇼​ "
    board[5][9] = "🇴 \n​"

    print("🇵 ​🇱 ​🇦​ 🇾 ​🇪​ 🇷​  🇴 ​🇳​ 🇪​   \n")
    for i in board:
        print ("".join(i))

    print("\n")

# conveerts from letter to number so we can track positon on board
def makeConversion(letter):
    if(letter == "A"):
        return 1
    elif(letter == "B"):
        return 2
    elif (letter == "C"):
        return 3
    elif (letter == "D"):
        return 4
    elif (letter == "E"):
        return 5
    elif (letter == "F"):
        return 6
    elif (letter == "G"):
        return 7
    elif (letter == "H"):
        return 8
    elif (letter == "I"):
        return 9

# ask first player where he wants to put his ships 
def makeShipPlayer1():


    corectPick = True
    while corectPick:
        corectPick = False
        
        shipNr = input(" Enter row and columns:")
        
        shipRow = shipNr[0]
        try:
            shipCol = makeConversion(str(shipNr[1]))
        except:
            print("Try again to enter your 3 ship positions")
            makeShipPlayer1()
            continue
        if(int(shipRow) > 4 or shipCol == None):
            print(" ERROR you didn't pick as instructed")
            corectPick = True
        else:
            return int(shipRow),shipCol
                

def makeShipPlayer2():
    #make ship for player2 , we need to chef if row is 5-9
    #we need both Row and Column for changing in Board
    corectPick = True
    while corectPick:
        corectPick = False
        
        shipNr = input(" Enter row and columns:")
        shipRow = shipNr[0]
        try:
            shipCol = makeConversion(str(shipNr[1]))
        except:
            print("Try again to enter your 3 ship positions")
            makeShipPlayer2()
            continue

        if(int(shipRow)  <= 5 or shipCol == None):
            print("error you didn't pick as instructed")
            corectPick = True
        else:
            return int(shipRow),shipCol

def strikePlayer1():
    
    corectPick = True
    while corectPick:
        corectPick = False
        print("\n 1. Player One:")
        print(" Example: 6C, 8A, 7E\n")
        print("      Enter attack position from 6 to 9 and column from A to I \n")
        shipNr = input(" Enter row and columns:")
        shipRow = shipNr[0]
        try:
            shipCol = makeConversion(str(shipNr[1]))
        except:
            print(" Try again to enter your ship positions")
            strikePlayer1()
            continue                        
        if (int(shipRow) <= 5 or shipCol == None):
            print("error you didn't pick as instructed")
            corectPick = True
        else:
            return int(shipRow), shipCol

def strikePlayer2():
    corectPick = True
    while corectPick:
        corectPick = False
        print("\n 2. Player Two: ")
        print(" Example: 1A, 3E, 2D\n")
        print("      Enter attack position from 1 to 4 and column from A to I \n")
        shipNr = input(" Enter row and columns:")
        shipRow = shipNr[0]
        try:
            shipCol = makeConversion(str(shipNr[1]))
        except:
            print(" Try again to enter your ship positions")
            strikePlayer2()
            continue
        if (int(shipRow) >= 5 or shipCol == None):
            print("error you didn't pick as instructed")
            corectPick = True
        else:
            return int(shipRow), shipCol

def gamePlay():

    winnerPlayer1 = 0
    winnerPlayer2 = 0
    while (winnerPlayer1 != 3 or winnerPlayer2 != 3):
        os.system('clear')
        banner()
        boardS()

        strikePlayer = strikePlayer1()
        if((strikePlayer == firstShipPlayer2) or (strikePlayer == secondShipPlayer2) or (strikePlayer == thirdShipPlayer2)):
            board[int(strikePlayer[0])][int(strikePlayer[1])] = "🇽​ "
       
            winnerPlayer1 += 1
            print("\n\n You hit ship {0} from Player 2\n\n".format(winnerPlayer1))
            time.sleep(3)
            os.system('clear')
            if(winnerPlayer1 == 3):
                banner()
                
                boardS()
                print('''PLAYER ONE IS THE WINNER''')
                break
          
        else:
   
            board[int(strikePlayer[0])][int(strikePlayer[1])] = "  "

            print("\n\n You missed\n\n")
            time.sleep(3)
              
        os.system('clear')   
        banner()
       
        boardS()
        strikePlayerTwo = strikePlayer2()
        
        if((strikePlayerTwo == firstShipPlayer1) or (strikePlayerTwo == secondShipPlayer1) or (strikePlayerTwo == thirdShipPlayer1)):
            board[int(strikePlayerTwo[0])][int(strikePlayerTwo[1])] = "🇽​ "
            winnerPlayer2 += 1

            print("\n\n You hit ship {0} from Player 1\n\n".format(winnerPlayer2))    
            time.sleep(3)
            os.system('clear')
            if(winnerPlayer2 == 3):
                banner()

                boardS()
                print('''PLAYER TWO IS THE WINNER''')
                break

      
        else:
            board[int(strikePlayerTwo[0])][int(strikePlayerTwo[1])] = "  "
            
            print("\n\n You missed\n\n")
            time.sleep(3)  
 


# graphics 
banner()
boardS()

# player one input
print(" Player One")
print("\n You need to enter ship position from 1 to 4 and column from A to I")
print(" Example: 1A, 3E, 2D\n")
firstShipPlayer1 = makeShipPlayer1()
secondShipPlayer1 = makeShipPlayer1()

# checks if the second ship has the same position as the first ship
checkIfSame = True
while checkIfSame:
    checkIfSame = False
    if(secondShipPlayer1 == firstShipPlayer1):
        print("You entered ship on same position")
        secondShipPlayer1 = makeShipPlayer1()
        checkIfSame = True
    

thirdShipPlayer1 = makeShipPlayer1()


# checks if the second ship has the same position as the first and third ship
checkIfSame2 = True
while checkIfSame2:
    checkIfSame2 = False
    if(thirdShipPlayer1 == firstShipPlayer1 or thirdShipPlayer1 == secondShipPlayer1):
        print(" You entered ship on same position")
        thirdShipPlayer1 = makeShipPlayer1()
        checkIfSame2 = True

os.system('clear')

banner()
boardS()


print(" Player Two")
print("\n You need to enter ship position from 6 to 9 and column from A to I")

print(" Example: 6C, 8A, 7E\n")

firstShipPlayer2 = makeShipPlayer2()

secondShipPlayer2 = makeShipPlayer2()

# checks if the second ship has the same position as the first ship
var1 = True
while var1:
    var1 = False
    if(secondShipPlayer2 == firstShipPlayer2):
        print(" You entered ship on same position")
        secondShipPlayer2 = makeShipPlayer2()
        var1 = True

thirdShipPlayer2 = makeShipPlayer2()

# checks if the second ship has the same position as the first and third ship

var2 = True
while var2:
    var2 = False
    if(thirdShipPlayer2 == firstShipPlayer2 or thirdShipPlayer2 == secondShipPlayer2):
        print(" You entered ship on same position")
        thirdShipPlayer2 = makeShipPlayer2()
        var2 = True


gamePlay()

