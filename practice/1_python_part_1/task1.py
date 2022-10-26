"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any

#list of numbers
numbers = ['1', '2', '3', '4', '15', '25', '22', '354']
numbers.remove ('1')

print ('updated list', numbers)

def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    ...
