SEKRET = "password"


def check_password():
    '''() -> bool

       Return True iff the correct password is entered.
    '''

    tries = 0
    # Try this at home! See what happens when you move "tries < 2" after
    # the call to input.
    while tries < 2 and not input("Enter your password: ") == SEKRET:
        print("Wah. Wah.")
        print("Try again.")
        tries = tries + 1

    return tries != 2


## If the Python docstring for input followed our design recipe, it
## might look something like this:
##
## def input(prompt):
##    '''(str) -> str
##
##    Print prompt and return whatever the user enters at the
##    keyboard -- not including the newline character.
##    '''
##
##    # Keyboard-handling magic

# check_password()

def is_prime(n):
    '''(int) -> bool

       Return True iff n is a prime number.

       >>> is_prime(3)
       True
       >>> is_prime(35)
       False
    '''

    i = 2

    while n > i:
        if n % i != 0:
            i = i + 1
            return False
    return True


def prime_factor(n):
    '''(int) -> NoneType

       Print all the prime factors of n.

       >>> prime_factor(5)
       5
       >>> prime_factor(24)
       2
       2
       2
       3
    '''

    divisor = 2
    while n > 1:
        if n % divisor == 0:
            print(divisor)
            n = n // divisor
        else:
            divisor = divisor + 1


    # Take-home exercise: make this check 2 as a divisor and then
    # only odd numbers. (Difficulty: medium)
    # Take-home exercise: make this check up to the square root of n.
    # (Difficulty: hard)

def whatever():
    x = True
    y = True
    z = 2
    # We need a notion of "progress" towards making
    # the expression following the while loop False.
    # Otherwise, we get stuck in an infinite loop (without
    # a return statement inside)
    while z < 5:
        z = 5


def is_digit(s):
    '''(str) -> bool

       Return True iff s is a single digit.

       >>> is_digit('a')
       False
       >>> is_digit('3')
       True
       >>> is_digit('54')
       False
    '''
    return s in '123456890' and len(s) == 1


def count_vowels(string):
    '''(str) -> int

       Return the number of vowels in string.

       >>> count_vowels('hello')
       2
       >>> count_vowels('123456')
       0
    '''

    vowels = 0

    idx = 0
    while idx < len(string):
        if string[idx] in 'aeoiuAEIOU':
            vowels = vowels + 1
        idx = idx + 1

    return vowels


def string_from_position(string, pos):
    '''(str, int) -> str

       Return the substring of string that begins at index pos.

       >>> string_from_position('hello', 2)
       'llo'
       >>> string_from_position('hello', -2)
       'lo'
       >>> string_from_position('hello', 100)
       ''
    '''

    # Try writing this string-slicing function at home!
    # (Difficulty: hard)


def contains(string1, string2):
    '''(str, str) -> bool

       Return whether string1 is contained in string2.

       >>> contains('hello', 'You say goodbye, I say hello.')
       True
       >>> contains('You say goodbye, I say hello.', 'hello')
       False
    '''

    # Try writing "in" at home.
    # (Coding difficulty: downright nasty unless you think about it...
    # then it's medium difficulty)
