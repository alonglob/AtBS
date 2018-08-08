
turn = 'X' #  start with Xs' turn

# board is the dictionary that holds the value of each location on the board, as the keys:
board = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
         'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
         'bot_L': ' ', 'bot_M': ' ', 'bot_R': ' '}


def print_board(board):  # creates a print layout do display the game graphically
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['bot_L'] + '|' + board['bot_M'] + '|' + board['bot_R'])


def check_victory(board, turn):  # checks if the move thats being made will end the game.
    if board['top_L'] == turn:
        if board['top_M'] == turn:
            if board['top_R'] == turn:
                return True

        if board['mid_L'] == turn:
            if board['bot_L'] == turn:
                return True

        if board['mid_M'] == turn:
            if board['bot_R'] == turn:
                return True

    if board['top_M'] == turn:
        if board['mid_M'] == turn:
            if board['bot_M'] == turn:
                return True

    if board['top_R'] == turn:
        if board['mid_R'] == turn:
            if board['bot_R'] == turn:
                return True

        if board['mid_M'] == turn:
            if board['bot_L'] == turn:
                return True

    if board['top_R'] == turn:
        if board['mid_R'] == turn:
            if board['bot_R'] == turn:
                return True

    if board['mid_L'] == turn:
        if board['mid_M'] == turn:
            if board['mid_R'] == turn:
                return True

    if board['bot_L'] == turn:
        if board['bot_M'] == turn:
            if board['bot_R'] == turn:
                return True

    else:
        return False


counter = 0  # start counting the moves being made
while counter < 9:  # end the game after 9 moves were made
    print(str(turn) + ' is up! whats your move?')
    move = input()

    if move not in board.keys(): # make sure its a legal move
        print('invalid move call, check again!')  # the value entered isent a key
        continue
    elif board[move] !=  ' ':
        print('invalid move,  check again!')  # the value entered is already filled with a value
        continue

    board[move] = turn
    print_board(board)

    if counter >= 3:
        check = check_victory(board,turn)
        if check == True:
            print(turn + ' has won the game!')
            break

    if turn == 'X':
        turn = 'O'
        counter += 1
    else:
        turn = 'X'
        counter += 1

    if counter == 8:
        print('game over, no winner!')

