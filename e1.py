def dollar_amount(nickels, dimes, quarters, loonies, toonies):
    '''(int, int, int, int, int) -> str

    Return a str with the value of the coins nickels, dimes, quarters, loonies,
    and toonies in cents. The str must be of the form "# cents" where # is the
    total value of the coins.    
    
    A nickel is worth 5 cents.
    A dime is worth 10 cents.
    A quarter is worth 25 cents.
    A loonie is worth 1 dollar (100 cents).
    A toonie is worth 2 dollars (200 cents).
    
    All arguments will be at least zero (0).
    
    Example calls from the shell:
    
    >>> dollar_amount(30, 0, 0, 0, 0)
    '150 cents'
    >>> dollar_amount(0, 1, 0, 5, 1)
    '710 cents'
    '''
5


def smallest_majority(group_size):
    '''(int) -> int

    Return the number of votes from a group of size group_size required for a
    strict majority. A strict majority occurs when more than half of a group
    votes in the same way.

    group_size must be greater than zero (0).

    Hint: How many votes does the minority have at most?
    
    Example calls from the shell:
    
    >>> smallest_majority(100)
    51
    >>> smallest_majority(101)
    51
    >>> smallest_majority(8)
    5
    
    '''



def phone_bill(free_minutes, cents_per_minute, minutes_used):
    '''(int, int, int) -> float

    Return the amount owed on a phone bill in dollars in a particular month if
    minute_used minutes are used and billed at cents_per_minute cents per minute
    with the first free_minutes minutes free.

    All arguments will be at least zero (0).

    Hint: You may find the min() and/or max() functions useful. See lecture
    notes on expressions + variables for example usage.

    Example calls from the shell:

    >>> phone_bill(0, 15, 0)
    0.0
    >>> phone_bill(0, 15, 20)
    3.0
    >>> phone_bill(100, 15, 55)
    0.0
    >>> phone_bill(100, 15, 110)
    1.5
    '''

