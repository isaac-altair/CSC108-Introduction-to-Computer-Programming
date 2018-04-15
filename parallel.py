def average_temp(high_temps, low_temps):
    '''(list of numbers, list of numbers) -> list of floats
    
       high_temps and low_temps are daily high and low temperatures for
       a series of days.
       Return a new list of temperatures where each element is the
       daily average.
       
       >>> average_temp([26, 27, 27, 28, 27, 26], [20, 20, 20, 20, 21, 21])
       [23.0, 23.5, 23.5, 24.0, 24.0, 23.5]
    '''
    averages = []
    for idx in range(len(high_temps)):
        averages.append((high_temps[idx] + low_temps[idx]) / 2)

    # alternately
##    idx = 0
##    while idx < len(high_temps):
##       averages.append((high_temps[idx] + low_temps[idx]) / 2)
##       idx = idx + 1
    
    return averages


### Take-home exercise
### Modify this function to check to see if one list is a shallow copy
### of the other.
### Difficulty: Easy.
def first_mismatch(lst1, lst2):
    '''(list of objects, list of objects) -> int
    
       Return the index of the first item at which the values of lst1 and lst2
       differ. Return -1 if no differences are found.
       
       >>> first_mismatch(['a', 'b', 'c'], ['a', 'd', 'c'])
       1
       >>> first_mismatch(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
       3
       >>> first_mismatch(['a', 'b', [1]], ['a', 'b', [1]])
       -1
    '''

    shorter = min(len(lst1), len(lst2))
    for idx in range(shorter):
        if lst1[idx] != lst2[idx]:
            return idx

    if len(lst1) == len(lst2):
        return -1

    return shorter

