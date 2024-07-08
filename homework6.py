my_dict = {'Denis': 1999, 'Ivan': 2003, 'Vlad': 2000}
print('Dict:', my_dict)
print('Existing value:',my_dict.get('Ivan'))
print('Not existing value:', my_dict.get('Petr'))
my_dict.update({'Alex':1980,'Max':2001})
print('Modified dictionary:',my_dict)
a = my_dict.pop('Ivan')
print('Deleted value:',a)

my_set = {1, 1, 2, 4, 4, 99, 99,'Ivan'}
print('Set:', my_set)
my_set.update({'Felix', 3, 77})
my_set.discard(4)
print('Modified set:', my_set)
