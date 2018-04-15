def add_item_to_plate(customers_plate, item):
    '''(list of str, str) -> NoneType
        
       Add item to the end of customers_plate.
       
       >>> add_item_to_plate(['salad'], 'soup')
    '''

    customers_plate.append(item)

bobs_plate = []
roberts_plate = bobs_plate

add_item_to_plate(bobs_plate, 'waffle')
# print(bobs_plate)
# print(roberts_plate)
# print(customers_plate)

twin_lists = [
                ['a', 'b', 'c'],
                ['a', 'b', 'c']
              ]

bobs_list = twin_lists[0]
bobs_list[0] = 'q'
roberts_list = twin_lists[0]
roberts_list[2] = 'd'
roberts_list = ['x', 'y', 'z']

print(twin_lists)
