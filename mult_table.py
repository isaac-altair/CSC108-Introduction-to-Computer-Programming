MAX_TABLE = 9

def print_mul(a, b):
    '''(number, number) -> NoneType
    
       Print out the original values of a and b and their product.
    '''

    print(str(a) + ' times ' + str(b) + ' is ' + str(a * b))


def print_x_times_table(x):
    '''(number, number) -> NoneType
    
       Print out the times table for x.
    '''
    i = 1
    while i <= MAX_TABLE:
        print_mul(x, i)
        i = i + 1


def print_mul_table():
    i = 1
    while i <= MAX_TABLE:
        print_x_times_table(i)
        i = i + 1


# a = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(str(a) + ' * ' + str(b) + ' = ' + str(a*b))
#         b = b + 1
#     a = a + 1


#print_mul_table()

### Take-home: Write function that prints out table in table form.
### Tip: help(str.rjust) -- or write your own function -- it was part of the
### optional week 4 lab questions.
#    1    2    3    4    5    6    7    8    9   10   11   12 
#    2    4    6    8   10   12   14   16   18   20   22   24 
#    3    6    9   12   15   18   21   24   27   30   33   36 
#    4    8   12   16   20   24   28   32   36   40   44   48 
#    5   10   15   20   25   30   35   40   45   50   55   60 
#    6   12   18   24   30   36   42   48   54   60   66   72 
#    7   14   21   28   35   42   49   56   63   70   77   84 
#    8   16   24   32   40   48   56   64   72   80   88   96 
#    9   18   27   36   45   54   63   72   81   90   99  108 
#   10   20   30   40   50   60   70   80   90  100  110  120 
#   11   22   33   44   55   66   77   88   99  110  121  132 
#   12   24   36   48   60   72   84   96  108  120  132  144

def separate_line(lst):
    i = 0
    while i < len(lst):
        element = lst[i]
        i = i + 1
        print(element)

##def column_print(lst):
##    j = 0
##    x = 2
##    while j < MAX_TABLE:
##        lst.append(lst[j] * x)
##        j = j + 1
##    print(lst)

def mult_table(length):
    i = 0
    while i < length:
        i = i + 1
        j = 0
        len_str = ''
        while j < length:
            j = j + 1
            len_str = len_str + str(i * j).rjust(len(str(length ** 2)) + 1) + ' '
        print(len_str)
            
            
        
        
    
                    
            
            
    
    
                    
