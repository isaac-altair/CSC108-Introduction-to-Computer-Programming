def is_divisible(n, lst):
    '''(int, list of ints) -> bool

       Return True iff n is evenly divisible by at least one element in lst.

       >>> is_divisible(10, [3, 4])
       False
       >>> is_divisible(10, [2, 3])
       True
    '''

    idx = 0

    while idx < len(lst):
        # What happens if we reverse the == to != and flip Trues and Falses?
        if n % lst[idx] == 0:
            return True
        idx = idx + 1

    return False


def is_divisible(n, lst):
    '''(int, list of ints) -> bool

       Return True iff n is evenly divisible by at least one element in lst.

       >>> is_divisible(10, [3, 4])
       False
       >>> is_divisible(10, [3, 4, 5, 6, 7])
       True
       >>> is_divisible(10, [5, 3, 2])
       True
    '''

    idx = 0
    
    ### found_divisor is an example of what we call a flag.
    ### A flag is used to signal a condition.
    found_divisor = False
    
    while idx < len(lst):
        found_divisor = found_divisor or (n % lst[idx] == 0)
        idx = idx + 1

    return found_divisor



### Take-home exercise. Complete the following function. This function should
### keep a list and only check for prime divisors. For example, to see if
### 143 is prime, it should only check 2, 3, 5, 7, 11
### (note that 9 was not checked).
def primes_list(n):
    '''(int) -> (list of ints)
    
       Return a list of the first n prime numbers.
       
       >>> primes_list(5)
       [2, 3, 5, 7, 11]
    '''  



