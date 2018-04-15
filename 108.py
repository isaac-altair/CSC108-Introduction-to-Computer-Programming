def read_menu(menu_file):
    '''(file open for reading) -> dict of int to str

    Read menu_file; each menu item in the restaurant has a number and a name.
    The resulting dictionary maps numbers to names.
    
    Sample input file:
       1 Fried rice
       2 Plain white rice
       3 Plain brown rice
      10 Chive dumpling (steamed)
      11 Pork and shrimp dumpling (steamed)
      12 Mushroom dumpling (steamed)
      13 Pork and bitter melon dumpling (steamed)
      14 Cherry dumpling (steamed)
      20 Pork and shrimp dumpling (fried)
      21 Pork dumpling (fried)
     101 Bubble tea
     102 Ice tea
    '''
    menu = {}
    f = menu_file
    line = f.readline().strip().split()
    while len(line) != 0:
        value = ''
        for item in line[1:]:
            value += " " + item
        menu[int(line[0])] = value
        line = f.readline().strip().split()
    return menu

def contains_duplicate_values(in_dict):
    '''(dict) -> boolean

    Return True iff in_dict has two or more keys that refer to objects that
    have the same value.

    >>> contains_duplicate_values({'a': 9, 'b': '9', 'c': 7, 9: True})
    False
    >>> contains_duplicate_values({'a': 9, 'b': 9, 'c': 7})
    True
    '''


def trace_lineage(family_tree, lineage):
    '''(dict, list of strs) -> boolean

    family_tree is a dict of people to another dictionary. The keys of each
    dictionary are peoples' names. The value dictionary is another family
    tree dictionary of children for the associated key. For example,
    
    {'Bob': {}, 'Margaret': {}}
    
    shows that Bob and Margaret both have no children.
    
    {'Bob': {'Simon': {'Laura': {}}, 'Lisa': {}}, 'Margaret': {}}
    shows that Bob has two children: Simon and Lisa. Simon has a single child,
    Laura.

    Return True iff lineage specifies a list of names who are directly related
    in a chain of parent-child relationships (not child-parent) beginning from
    the first generation listed.
    
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      ['Bob'])
    True
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      ['Margaret'])
    True
    
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      ['Bob', 'Simon', 'Laura'])
    True
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      ['Bob', 'Laura'])
    False
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      ['Malbert'])
    False
    >>> trace_lineage({'Bob': {'Simon': {'Laura': {}},
                               'Lisa': {}},
                       'Margaret': {}},
                      [])
    True
    '''

if __name__ == "__main__":
    f = open("menufile.txt")
    print read_menu(f)