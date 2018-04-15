# write a loop that prints out the numbers from 0 to 7 (not including)


##while True:
##    print ('Hello')
##    print("N")
##print('done')


##i = 0
##while i < 42:
##    print ('Hello')
##    print("N")
##print('done')

##i = 0
##while i < 42:
##    print ('Hello')
##    print("N")
##    i = i + 1
##print('done')

##i = 0
##while i < 7:
##    print(i)
##    i = i + 1
##print('done')

##j = 0
##while j < 6:
##    i = 0
##    while i < 7:
##        print(str(i) + ',' + str(j))
##        i = i + 1
##    j = j + 1
##print('done')

##j = 0
##while j < 6:
##    i = 0
##    while i < 12:
##        a = 0
##        while a < 24:
##            b = 0
##            while b < 30:
##                c = 0
##                while c < 36:
##                    print(str(c) + ',' + str(b) + ',' + str(a) + ',' + str(i) + ',' + str(j))
##                    c = c + 1
##                b = b + 1
##            a = a + 1
##        i = i + 1
##    j = j + 1
##print('done')
    
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
##    while j < 42:                               #Right
##        new_board = new_board + '|' + board[j]  #Right
##        j = j + 1                               #Right
##    return new_board + '|'                      #Right
