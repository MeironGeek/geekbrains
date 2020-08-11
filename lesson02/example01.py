test_list = ['T', 'e', 'l', 'L', 1, 'H', 5]
test_tuple = tuple(test_list)
test_set = set(test_tuple)
test_frozen = frozenset({3, 5, 5, 7, 1})
test_dict = {'name': 'Igor', 'age': 29}

types_list = [25,
              'Test',
              0,
              '0',
              True,
              None,
              b'hello',
              test_list,
              test_tuple,
              test_set,
              test_frozen,
              test_dict
              ]

for elem in types_list:
    print(type(elem))
