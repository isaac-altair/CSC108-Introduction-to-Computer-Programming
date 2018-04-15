def temperature_to_attire(weather):
    '''(list of ints) -> list of strs

    Modify and return the list passed in as weather, replacing each temperature
    (in degrees Celsius) in the list with the type of clothing to be worn
    for that temperature.

    A t-shirt day is any day above 18 degrees Celsius and a sweater day is
    anything 18 degrees Celsius or less.

    >>> temperature_to_attire([19, 23, 15, 18, 20])
    ['t-shirt', 't-shirt', 'sweater', 'sweater', 't-shirt']
    '''
    for idx in range(len(weather)):        
        if weather[idx] <= 18:
            weather[idx] = 'sweater'
        else:
            weather[idx] = 't-shirt'
    return weather
        

def common_items(lst1, lst2):
    '''(list of objects, list of objects) -> int

    Return the number of items that appear in the same position of both lst1
    and lst2.

    >>> common_items(['a', 'b', 'c', 'd'], ['a', 'x', 'b', 'd'])
    2
    >>> common_items(['a', 'b', 'c', 'd', 'e'], ['a', 'x', 'b', 'd'])
    2
    '''
    num_same = 0
    for idx in range(min(len(lst1), len(lst2))):
        if lst1[idx] == lst2[idx]:
            num_same += 1
    return num_same          
          

def find_first_even(lst):
    '''(list of [list of ints]) -> int

    Return the index of the first list in lst that contains an even number.
    Return -1 if no such item is found.
    
    >>> find_first_even([[9, 1, 3], [2, 5, 7], [9, 9, 7, 2]])
    1
    >>> find_first_even([[1, 3, 5], [7, 9], [1, 0]])
    2
    >>> find_first_even([[1, 3, 5]])
    -1
    '''
    for idx1 in range(len(lst)):
        for idx2 in range(len(lst[idx1])):
            if lst[idx1][idx2] % 2 == 0:
                return idx1
    return -1