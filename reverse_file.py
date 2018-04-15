def reverse_groups(list_of_groups):
    '''(list of [list of str]) -> str
    
       Returns a string that contains the reversed groups of some text.
       The original lists must remain unmodified.
       
       >>> reverse_groups([['A', 'B', 'C'], ['D', 'E', F']])
       'CBAFED'
       
    '''
    output_string = ''
    for sub_list in list_of_groups:
        sub_list.reverse()
        for letter in sub_list:
            output_string = output_string + letter           
    return output_string