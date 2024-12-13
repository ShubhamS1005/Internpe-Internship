import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "\U0001F535":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "\U0001F534":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
   
    for x in range(rows):
        for y in range(cols - 3):
            if (
                gameBoard[x][y] == chip and
                gameBoard[x][y + 1] == chip and
                gameBoard[x][y + 2] == chip and
                gameBoard[x][y + 3] == chip
            ):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

   
    for x in range(rows - 3):
        for y in range(cols):
            if (
                gameBoard[x][y] == chip and
                gameBoard[x + 1][y] == chip and
                gameBoard[x + 2][y] == chip and
                gameBoard[x + 3][y] == chip
            ):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    
    for x in range(rows - 3):
        for y in range(3, cols):
            if (
                gameBoard[x][y] == chip and
                gameBoard[x + 1][y - 1] == chip and
                gameBoard[x + 2][y - 2] == chip and
                gameBoard[x + 3][y - 3] == chip
            ):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

   
    for x in range(rows - 3):
        for y in range(cols - 3):
            if (
                gameBoard[x][y] == chip and
                gameBoard[x + 1][y + 1] == chip and
                gameBoard[x + 2][y + 2] == chip and
                gameBoard[x + 3][y + 3] == chip
            ):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False

def coordinateParser(inputString):
    if len(inputString) != 2 or inputString[0] not in possibleLetters or not inputString[1].isdigit():
        print("Invalid input. Format should be like A1, B2, etc.")
        return None
    col = possibleLetters.index(inputString[0])
    row = int(inputString[1])
    if 0 <= row < rows:
        return [row, col]
    else:
        print("Row out of bounds. Must be between 0 and 5.")
        return None

def isSpaceAvailable(intendedCoordinate):
    return gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == ""

def gravityChecker(col):
    for row in reversed(range(rows)):
        if gameBoard[row][col] == "":
            return row
    return None

leaveLoop = False
turnCounter = 0
while not leaveLoop:
    printGameBoard()
    currentChip = "\U0001F535" if turnCounter % 2 == 0 else "\U0001F534"
    if turnCounter % 2 == 0:
        while True:
            spacePicked = input("\nChoose a column (A-G): ").upper()
            if spacePicked in possibleLetters:
                col = possibleLetters.index(spacePicked)
                row = gravityChecker(col)
                if row is not None:
                    modifyArray([row, col], currentChip)
                    break
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid input. Choose a column (A-G).")
    else:
        while True:
            col = random.randint(0, cols - 1)
            row = gravityChecker(col)
            if row is not None:
                modifyArray([row, col], currentChip)
                break
    if checkForWinner(currentChip):
        printGameBoard()
        break
    if all(gameBoard[0][col] != "" for col in range(cols)):
        print("\nIt's a tie! The board is full.")
        printGameBoard()
        break
    turnCounter += 1
