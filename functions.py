def human_to_dog_years(human_years):
    ''' (int) -> int

    Return the number of dog years equivalent to human_years.

    One human year is the equivalent of seven dog years.

    >>> human_to_dog_years(3)
    21
    '''
   
    human_to_dog_years = human_years * 7
    
    return (human_to_dog_years)

    
    #human_years = human_years * 7
    
    #print (human_to_dog_years(3))
    


def instructors_needed(num_courses):
    ''' (int) -> int

    Return the minimum number of instructors required to teach num_courses
    courses.

    Each instructor teaches up to 3 courses.

    >>> instructors_needed(3)
    1
    >>> instructors_needed(10)
    4
    '''
    instructors_needed = (num_courses // 3) + (num_courses % 3)
    
    #return (instructors_needed)
    
    #instructors_needed = num_courses // 3 + 1
    
    return (instructors_needed)



def cookies_needed(num_adults, num_teens, num_children):
    ''' (int, int, int) -> int

    Return the number of cookies needed to feed num_adults adults, num_teens
    teens, and num_children children.
    Each adult gets 3 cookies, each teenager gets 5, and each child gets 2.

    >>> cookies_needed(2, 3, 1)
    23
    '''
    num_adults = num_adults * 3
    num_teens = num_teens * 5
    num_children = num_children * 2
    cookies_needed = num_adults + num_teens + num_children
    
    return (cookies_needed)



def cookie_sugar_needed(num_adults, num_teens, num_children):
    ''' (int, int, int) -> float

    Return the number of grams of sugar needed to make cookies for num_adults
    adults, num_teens teens, and num_children children.

    Each adult gets 3 cookies, each teenager gets 5, and each child gets 2.
    Each cookie needs 0.0625 grams of sugar.

    >>> cookie_sugar_needed(2, 3, 1)
    1.4375
    '''
    
    cookie_sugar_needed = cookies_needed(num_adults, num_teens, num_children) * 0.0625
        
    return (cookie_sugar_needed)    
