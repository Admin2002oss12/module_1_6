my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Kamila'))
my_dict.update({'Viktor': 1998,
                'Sasha': 1988})
print(my_dict.pop('Egor'))
print(my_dict)
#
#
my_set = {1, 'Яблоко', 42.314}
print(my_set)
my_set.update((2, 4, 9))
my_set.discard('Яблоко')
print(my_set)
