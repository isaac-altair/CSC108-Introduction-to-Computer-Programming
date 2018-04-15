def in_century(year, century):
    '''(int, int) -> bool

    Return True iff year is in century.

    Remember, for example, that 1900 is the last year of the 19th century,
    not the beginning of the 20th.

    year will be at least 1.

    >>> in_century(1994, 20)
    True
    >>> in_century(2013, 20)
    False
    '''
            #(century > 0 and (95.0 < float(year / century) <= 100.0)
            #or 0.0 < year <= 100.0 and century == 1.0
            #or 100.0 < year <= 100.0 + 100.0 and century == 1.0 + 1.0
            
    return (century * 100 - 99 <= year <= century * 100)


accountant = 42600
dentist = 81500
engineer = 73200
programmer = 48700
retail = 23000


def salary(job, years_of_service):
    '''(str, int) -> float

    Return the salary (in dollars) of a person holding job for
    years_of_service.

    Each year, a person receives a 5% increase in salary over his/her previous
    year. The starting salary for various jobs:
        accountant                                  $42 600
        dentist                                     $81 500
        engineer                                    $73 200
        programmer                                  $48 700
        retail                                      $23 000

    years_of_service will be at least 0.

    >>> salary('retail', 0)
    23000.0
    >>> salary('retail', 2)
    25357.5
    '''

    multiplier = 1.05 ** years_of_service
    if job == 'accountant':
        return accountant * multiplier
    elif job == 'dentist':
        return dentist * multiplier
    elif job == 'engineer':
        return engineer * multiplier
    elif job == 'programmer':
        return programmer * multiplier
    elif job == 'retail':
        return retail * multiplier
    else:
        return "Job does not exist"
              
    
small = 200
medium = 300
large = 400
jumbo = 600
promotional = jumbo + 1


def drink_size(volume):
    '''(number) -> str

    Return the size of a drink given the amount of volume of a beverage (in mL)
    served. If a volume does not correspond to a drink size, return "invalid".

    A kid-sized drink is any beverage of at least 100 mL but smaller
        than a large drink that isn't another drink size.
    A small drink contains 200 mL of beverage.
    A medium drink contains 300 mL of beverage.
    A large drink contains 400 mL of beverage.
    A jumbo drink contains 600 mL of beverage.
    A promotional-sized drink is any beverage larger than a large drink that
        isn't another drink size.

    >>> drink_size(-20)
    'invalid'
    >>> drink_size(200)
    'small'
    >>> drink_size(120)
    'kid-sized'
    '''
    
    if volume == 200:
        print 'small'
    elif volume == 300:
        print 'medium'
    elif 100 <= volume < 400:
        print 'kid-sized'
    elif volume == 400:
        print 'large'
    elif volume == 600:
        print 'jumbo'
    elif volume > 400:
        print 'promotional-sized'
    #else:
        #print 'invalid'

    
    
