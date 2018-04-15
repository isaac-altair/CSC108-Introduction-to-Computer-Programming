def sum_mass(mass_list):
    '''(list of [object, number]) -> number
    
       Return the sum of all the masses in mass_list where the mass is the
       second item in each element of lst.
       
       >>> sum_mass([['Hello', 3], [2, 5]])
       8
    '''

    idx = 0
    total = 0

    while idx < len(mass_list):
        total = total + mass_list[idx][1]
        idx = idx + 1

    return total

 
def metricize_list(lst):
    '''(list of [object, number]) -> NoneType
    
       Modify lst, converting the item at index 1 from lb to kg.
    
       >>> metricize_list([['Lou', 137], ['Pat', 112]])
    '''

    idx = 0

    while idx < len(lst):
        pair_weight_convert(lst[idx])
        idx = idx + 1

def pair_weight_convert(lst):
    '''(list [object, number]) -> NoneType
    
       Modify lst, converting the item at index 1 from lb to kg.
    
       >>> pair_weight_convert(['Lou', 137])
    '''

    lst[1] = lb_to_kg(lst[1])


def lb_to_kg(lb):
    '''(number) -> float
    
       Return an approximation of mass in lb converted to kg.
    
       >>> lb_to_kg(17.6)
       8.0
    '''

    return lb / 2.2


### Take-home exercise: make this work on nested lists using another loop.
### Difficulty: medium
def min_in_list(lst):
    '''(list of numbers) -> number

       Return the smallest value in lst.

       >>> min_in_list([156, 373, 2.9, -573, 12])
       -573
    '''

#    if len(lst) == 0:
#        return float('-infinity')

    ### This is for a list of list of numbers
    # Expand lst to remove nesting
    long_list = []
    idx = 0
    while idx < len(lst):
        long_list = long_list + lst[idx]
        idx = idx + 1

    lst = long_list

    # ... more comments
        
    smallest = lst[0]

    idx = 1
    while idx < len(lst):
        if lst[idx] < smallest:
            smallest = lst[idx]

        idx = idx + 1

    return smallest

people_masses = [['Bob', 138],
                 ['Boberta', 125],
                 ['Sam', 163],
                 ['Pat', 112],
                 ['Danny', 121]]




metricize_list(people_masses)
print(people_masses)
