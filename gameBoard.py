
gameBoard = [{}, {}, {},
             {}, {}, {},
             {}, {}, {}
             ]


def checkWin(player):

    win = False

    def checkRows():
        nonlocal win
        indexInRow = 0
        rowScore = 0

        for i in gameBoard:
            indexInRow += 1
            if i and (i['player'] == player["name"]):
                rowScore += 1
                # print(f"row score: {rowScore}")
            if rowScore == 3:
                win = True
                # print("row win")
            if not indexInRow % 3:
                indexInRow = 0
                rowScore = 0

    def checkOverBoard(start, stop, step):
        nonlocal win
        score = 0
        for i in range(start, stop, step):
            if gameBoard[i] and (gameBoard[i]['player'] == player["name"]):
                score += 1
                # print(f"score: {score}")
            if score == 3:
                win = True
                # print("win")

    def checkColumns():
        checkOverBoard(0, 9, 3)
        checkOverBoard(1, 9, 3)
        checkOverBoard(2, 9, 3)

    def checkLeftRightDiagonal():
        checkOverBoard(0, 9, 4)

    def checkRightLeftDiagonal():
        checkOverBoard(2, 7, 2)

    checkColumns()
    checkLeftRightDiagonal()
    checkRightLeftDiagonal()
    checkRows()

    return win
