# The board dimensions.
WIDTH = 7
HEIGHT = 6

# The number of tokens that must be played in a row by a player in
# order to win.
WIN_LENGTH = 4

# The token symbols for the different players.
# There can be more than two players
PLAYERS = "XO"

def get_piece(board, x, y):
    '''(str, int, int) -> str

       Return the piece at position x, y on the board or the empty string
       if the space is empty.

       >>> get_piece('   XOX  XXXX                              ', 0, 2)
       ''
       >>> get_piece('   XOX  XXXX                              ', 0, 3)
       'X'
       >>> get_piece('   XOX  XXXX                              ', 0, 4)
       'O'
    '''

    # TODO: Complete this function.

    if x < WIDTH and y <HEIGHT:
        i = (x * 6 + y)
        position = board[i]
    else:
        return ''

    return(position)



# Make sure slope function adheres to requirements
# Note: since our Width is 7 and Height is 6, our 0<=x<7 and 0<=y<6
def slope(x, x_2, y, y_2):

    if x < WIDTH and x_2 < WIDTH and y < HEIGHT and y_2 < HEIGHT:
        delta_x = x - x_2
        delta_y = y - y_2
        slope = float("inf") if x == x_2 else delta_y / delta_x
        return slope
    else:
        print("Green Banana, Want Yellow Banana")
    


def extract_run(board, x, y, delta_x, delta_y, length):
    '''(str, int, int, int, int, int) -> str

       Return all the non-empty pieces on the board in a line of slope
       delta_y/delta_x starting from position x, y.

       >>> extract_run('     X    XO   XOO  XXOX                  ',
                       0, 5, 1, -1, 4)
       'XXXX'
       >>> extract_run('         123OXOXOX456                     ',
                       0, 2, 0, 1, HEIGHT)
       ''
    '''

    # TODO (Optional): Complete this function.
    # You do not need to complete this function for full marks, but you may
    # find it useful.

    # -1) Develope delta_x and delta_y. DONE #
    # 0) Develop the slope function. DONE    #
    # 1) Search for first 'X' in the string.
    # 2) Locate its index.
    # 3) Locate x and y values related to that index.
    # 4) If first X (with location (x, y)) is located, look for the second X with coordinate(x + 1, y - 1). Check if their slope is one. If yes, locate the third X,
    #       if not discontinue the process untill you find the next X.
    # 5) After locating the second X, locate the third X with coordinate (x+2, y - 2). Check if the slope is one. If yes, locate the fourth X, if not discontinue
    #       the process until you find the next X.
    # 6) After locating the third X, look for the fourth X with the coordinate (x + 3, y - 3). Check if the slope is one, if yes, print out 'XXXX'
    # 7) If X is not located, search for the first Y and run the same process until you get 'YYYY'
    # 8) Else return ''

##    want_X = "XXXX"
##    want_Y = "YYYY"
    
##    if x < 7 and y <6:
##        i = (y * 7 + x)

    # Find first X in the string
    if "X" in board:
        first_X = board.index("X") # Locate its index
        x = first_X % 7 # Locate x and y values pertaining to that index
        y = first_X // 7
        # Look for the second X with coordinate (x + 1, y - 1)
        second_X = 
    elif "Y" in board:
        
    else:
        return ''

    # Look for the second "X" with coordinates (x+1, y-1)
    
##    while i < len(board):
##        if ' ' != board[i]:
##            if 'X' == board[i]:
##                if slope(x, y, delta_x, delta_y) == 1 or -1:
##                    if (x + 3, y - 3) - (x, y) == (3, -3):
##                        return board[i]
##                    else:
##                        return ''
##            elif 'O' == board[i]:
##                if slope(x, y, delta_x, delta_y) == 1 or -1:
##                    if (x + 3, y - 3) - (x, y) == (3, -3):
##                        i = i + 1
##                        return board[i]
##                    else:
##                        return ''
##        else:
##            return ''
            
def _vertical_line():
    return "|"

def _horizontal_lines():
    return "\n_ _ _ _ _ _ _ _"

##def print_board(board):
##    '''(str) -> None
##
##       Display the board on the screen.
##
##       Note the blank line before and after the the board.
##
##       >>> print_board('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef')
##
##       Board:
##       |1|7|C|I|O|U|a|
##       |2|8|D|J|P|V|b|
##       |3|9|E|K|Q|W|c|
##       |4|0|F|L|R|X|d|
##       |5|A|G|M|S|Y|e|
##       |6|B|H|N|T|Z|f|
##       ---------------
##
##    '''
##    j = 0                                       #Right
##    new_board = ''                              #Right
##
##    while j < WIDTH * HEIGHT:                               #Right
##        new_board = new_board + '|' + board[j]  #Right
##        j = j + 6
##        while 
##
##    return new_board + '|'
##        
##
##def columnize_board(print_board):
##
##    k = 0
##    l = 0
##    m = 0
##    n = 0
##    o = 0
##    p = 0
##    x = 0
##    y = 0
##    row_0 = ''
##    row_1 = ''
##    row_2 = ''
##    row_3 = ''
##    row_4 = ''
##    row_5 = ''
##    while x < WIDTH and y < HEIGHT:
##        k = (x * 6 + y) * 2
##        while x < 7 and y < 1:
##            row_0 = row_0 + print_board[k]
##            k = k + 1
##        return row_0
##        l = (x * 6 + y + 1) * 2
##        while x < WIDTH and 0 < y < 2:
##            row_1 = row_1 + print_board[l]
##            l = l + 1
##        return row_1
##        m = (x * 6 + y + 2) * 2
##        while x < WIDTH and 1 < y < 3:
##            row_2 = row_2 + print_board[m]
##            m = m + 1
##        return row_2
##        n = (x * 6 + y + 3) * 2
##        while x < WIDTH and 2 < y < 4:
##            row_3 = row_3 + print_board[n]
##            n = n + 1
##        return row_3
##        o = (x * 6 + y + 4) * 2
##        while x < 7 and 3 < y < 5:
##            row_4 = row_4 + print_board[o]
##            o = o + 1
##        return row_4
##        p = (x * 6 + y + 5) * 2
##        while x < WIDTH and 4 < y < 6:
##            row_5 = row_5 + print_board[p]
##            k = k + 1
##        return row_5
##    columnized_board = row_0 + '\n' + row_1 + '\n' + row_2 + '\n' + row_3 + '\n' + row_4 + '\n' + row_5
##    return print(columnized_board)                      #Right
##    
##            
##def has_won(board):
##    # TODO: Complete this function and its docstring.
##    return False
##
##
##def insert_piece(board, column, player):
##    '''(str) -> str
##
##       Return a string representing the board if player inserts a piece
##       in column of board.
##
##       board must have free space in column.
##
##       >>> insert_piece('XXXXXX  OOOO                              ', 1, 'X')
##       'XXXXXX XOOOO                              '
##    '''
##
##    # TODO: Complete this function.
##    return board
##
##
##def next_player(cur_player):
##    # TODO: Complete this function and its docstring.
##    return PLAYERS[0]
##
##
##def get_column(board, player):
##    # TODO: Complete this function and its docstring.
##    input("PLACEHOLDER")
##    return 1
##
################################################################################
################################################################################
###############                                              ###################
###############    Do not change anything below this line    ###################
###############                                              ###################
################################################################################
################################################################################
##
##
##def board_filled(board):
##    '''(str) -> bool
##
##       Return True iff board contains no empty spaces.
##
##       >>> board_filled('   XOX  XXXX                              ')
##       False
##       >>> board_filled('ABCDEFGXXXXXABCDFGHXXXXXXXXXXXXXXXXXXXXXXX')
##       True
##    '''
##
##    while board != '':
##        if board[0] == ' ':
##            return False
##
##        board = board[1:]
##
##    return True
##
##
##def congratulate_winner(board, player):
##    '''(str, str) -> None
##
##       Print a congratulatory message to the player.
##    '''
##
##    print("Congratulations! " + player + " wins!")
##
##
##def draw_message(board):
##    '''(str) -> None
##
##       Print a message in the event of a draw. board is ignored.
##
##       >>> draw_message('')
##       Game ended in a draw.
##    '''
##
##    print("Game ended in a draw.")
##
##
##### Main program ###
##
##board = " " * WIDTH * HEIGHT
##player = PLAYERS[-1]
##
##while not has_won(board) and not board_filled(board):
##    player = next_player(player)
##    print_board(board)
##    column = get_column(board, player)
##    board = insert_piece(board, column, player)
##
##print_board(board)
##
##if has_won(board):
##    congratulate_winner(board, player)
##else:
##    draw_message(board)
